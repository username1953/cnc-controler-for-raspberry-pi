# hello_psg.py

import PySimpleGUI as sg
import os 

 
# Create the window
layout = [ [sg.Text("controler for raspberry Py")], [sg.Button("move foward")], [sg.Button("move backwards")], [sg.Button("Quit")], ]

            # Create the window
window = sg.Window("cnc control", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Quit" or event == sg.WIN_CLOSED:
        break




window.close()
     




     