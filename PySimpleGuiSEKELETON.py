import PySimpleGUI as sg

layout=[[sg.Input(),sg.Button('Ok'),sg.Button('cancel')]]

window=sg.Window('PySimpleGUI Frame',layout)

while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED:
        break
    
window.close()