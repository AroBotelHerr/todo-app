import functions
import FreeSimpleGUI as sg

label = sg.Text("Hello World")
input_box = sg.InputText(tooltip="Enter a to do")
add_button = sg.Button("Add")

window = sg.Window("Password Manager", layout=[[label,input_box , add_button]])
window.read()
window.close()