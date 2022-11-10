import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


todos = functions.get_todos()

st.title('My To-do App')
st.subheader('This are my to-do for today:')
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo.strip('\n'))
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo.strip('\n')]
        st.experimental_rerun()


st.text_input(label='Enter a todo',
              placeholder='Enter a todo...',
              label_visibility='hidden',
              on_change=add_todo,
              key='new_todo')

