import FreeSimpleGUI as sg



label1 = sg.Text("Select file to compress:")
input1 = sg.Input()
choose_buttton1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_buttton2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Zipper",
                   [[label1, input1, choose_buttton1],
                    [label2, input2, choose_buttton2],
                    [compress_button]])


window.read()
window.close()