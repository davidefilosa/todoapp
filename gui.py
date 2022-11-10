import functions

import PySimpleGUI as sg

label = sg.Text('Type a to-do')
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

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
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = functions.get_todos()
            i = todos.index(todo_to_edit)
            todos[i] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            i = todos.index(todo_to_complete)
            todos.pop(i)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()
