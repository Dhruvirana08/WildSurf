import PySimpleGUI as sg

sg.theme('NeutralBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Press cancel or close this window to exit')],
            [sg.Text('Enter the given animal and then click ok for more info:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Wild Surf', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Here is info on: ', values[0])
    #Maybe then check for all possibilieis?
    #if values[0]=='reindeer'
