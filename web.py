import streamlit as st
import functions

todos = functions.get_todos()

st.title('My To-do App')
st.subheader('This are my to-do for today:')
for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Enter a todo...')