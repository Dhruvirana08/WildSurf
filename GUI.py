import PySimpleGUI as sg

sg.theme('NeutralBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Would you like to learn more about this animal? ')],
            [sg.Text('Enter the given animal for more info or press Cancel to close'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Wild Surf', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Here is more information on: ', values[0])
    print("Head here to learn more: https://bit.ly/WildSurfAnimalFacts")
