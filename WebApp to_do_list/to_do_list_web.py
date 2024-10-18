import streamlit as st
import functions

print("At the begining")

todos = functions.get_todos("todos.txt")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)    

# def complete():
#     to_remove_todo = st.session_state[]


# title, subheader, write
st.title("ToDo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    
st.text_input("Enter a todo", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")

print("At the end")
st.session_state
