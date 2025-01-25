from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

import sys
from datetime import datetime

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        self.metric_option = QComboBox()
        self.metric_option.addItems(["Metric(Km)", "Imperial(Miles)"])

        time_label = QLabel("Time (Hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # add widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.output_label, 3, 0, 1, 3)
        grid.addWidget(self.metric_option, 0, 2)

        self.setLayout(grid)
    
    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance / time
        if self.metric_option.currentText() == "Metric(Km)":
            speed_metric = "kmph"
        else:
            speed_metric = "mph"

        self.output_label.setText(f"Average speed is {speed} {speed_metric}!")
        

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
