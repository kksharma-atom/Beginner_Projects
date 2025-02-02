from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import sqlite3
import mysql.connector
import os


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", 
                 password=os.getenv("MYSQL_ROOT_PASSWORD"), database="school"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, user =self.user,
                                             password=self.password, database=self.database)
        return connection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(400, 500)

        file_menu_item = self.menuBar().addMenu("&File")
        edit_menu_item = self.menuBar().addMenu("&Edit")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction(QIcon("icons/add.png"),"Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        search_student_action = QAction(QIcon("icons/search.png"),"Search", self)
        search_student_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_student_action)

        # Create status bar and add status bar elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):

        dialog = SearchDialog()
        dialog.exec()
    
    def edit(self):
        dialog = EditDialog()
        dialog.exec()
    
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()
class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Physics", "Chemistry", "Mathmatics", "Biology"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile number widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add a Submit button
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)        

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)", (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        parent_window.load_data()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        button = QPushButton("Search")
        button.clicked.connect(self.search_student)
        layout.addWidget(button)


        self.setLayout(layout)
    
    def search_student(self):
        # Get student name
        name = self.student_name.text()

        # Set up database connection
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()

        # Execute query
        cursor.execute("SELECT * FROM students WHERE UPPER(name) LIKE UPPER(%s)", ('%' + name + '%',))
        result = cursor.fetchall()

        # Convert query result to list of tuples
        rows = list(result)

        # Clear table selection
        parent_window.table.clearSelection()

        # Unpack each tuple
        for row_data in rows:
            student_id, student_name, course, mobile_no = row_data
            print(row_data)
        # Filter table items by student_name  
        # Here, items is a list and the elements of this list are 
        # objects of class QTableWidgetItem i.e. each cell of the 
        # table is an object of type QTableWidgetItem
        # Since, items is a list and even if it contains just one
        # element, it still needs to be iterated upon 
            items = parent_window.table.findItems(student_name, Qt.MatchFlag.MatchFixedString)
            print(items.__len__())
            print(type(items))
        # Highlight each name 
            for item in items:
                print(item)
                print(item.text())
                if student_name in item.text():
                    parent_window.table.item(item.row(), 1).setSelected(True)

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Get the index of the current selected row
        index = parent_window.table.currentRow()

        # Get current id
        self.student_id = parent_window.table.item(index, 0).text()
        # Get student name from selected row
        student_name = parent_window.table.item(index, 1).text()

        # Get course name
        selected_course_name = parent_window.table.item(index, 2).text()

        # Get mobile number
        mobile_number = parent_window.table.item(index, 3).text()

        # Add student name widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Physics", "Chemistry", "Mathmatics", "Biology", "Astronomy"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(selected_course_name)
        layout.addWidget(self.course_name)
        print(selected_course_name)

        # Add mobile number widget
        self.mobile = QLineEdit(mobile_number)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add a update button
        button = QPushButton("Update")
        button.clicked.connect(self.update_record)
        layout.addWidget(button)

        self.setLayout(layout)        
    
    def update_record(self):
    
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s", 
                        (self.student_name.text(),
                        self.course_name.itemText(self.course_name.currentIndex()),
                        self.mobile.text(),
                        self.student_id))
        connection.commit()
        cursor.close()
        connection.close()

        # Refresh the table 
        parent_window.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")
        self.setFixedWidth(250)
        self.setFixedHeight(125)

        # Get selected row index and student id
        index = parent_window.table.currentRow()
        self.student_id = parent_window.table.item(index, 0).text()

        layout = QGridLayout()

        confirmation_label = QLabel("Do you want to delete this record ?")
        yes_button = QPushButton("Yes")
        yes_button.clicked.connect(self.delete_record)
        no_button = QPushButton("No")
        no_button.clicked.connect(self.dialog_close)



        layout.addWidget(confirmation_label, 0, 0, 1, 2)
        layout.addWidget(yes_button, 1, 0)
        layout.addWidget(no_button, 1, 1)

        self.setLayout(layout)
    
    def delete_record(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", 
                        (self.student_id, ))
        connection.commit()
        cursor.close()
        connection.close()

        # Refresh the table 
        parent_window.load_data()

        self.close()

        confirmation_message = QMessageBox()
        confirmation_message.setWindowTitle("Success")
        confirmation_message.setText("The record was deleted successfully")
        confirmation_message.exec()
        
    def dialog_close(self):
        self.close()

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app was created during the course "The Python Mega course".
        Feel free to reuse this app
        """
        self.setText(content)

app = QApplication(sys.argv)
parent_window = MainWindow()
parent_window.load_data()
parent_window.show()
sys.exit(app.exec())
