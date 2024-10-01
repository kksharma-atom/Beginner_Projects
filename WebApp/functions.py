FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):

    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, "r") as file_local:
        return file_local.readlines()
    

def write_todos(todos_local, filepath=FILEPATH):

    """ Write the to-do items list in the text file"""

    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)

 
# The print function will be called only when functions.py files is executed. If function.py file is imported in some other file, then the print function will not run.
if __name__ == "__main__":
    print("Hello")
