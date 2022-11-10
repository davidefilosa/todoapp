import functions

import PySimpleGUI as sg

label = sg.Text('Type a to-do')
input_box = sg.InputText(tooltip='Enter a to-do')
add_button = sg.Button('Add')
layout =[[label], [input_box, add_button]]

window = sg.Window(title='My To-Do App', layout=layout)

window.read()
window.close()