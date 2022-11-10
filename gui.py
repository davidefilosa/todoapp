import functions

import PySimpleGUI as sg

label = sg.Text('Type a to-do')
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')
layout = [[label], [input_box, add_button]]

window = sg.Window(title='My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
