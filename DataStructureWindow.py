import PySimpleGUI as sg
import BSTWindow as bstw
import StackWindow as sw
import QueueWindow as qw

class DataStructureWindow:
    def __init__(self):
        self.create()

    def create(self):
        layout = [
                    [sg.Text("Pick Data Structure")],
                    [sg.Button("Binary Search Tree")],
                    [sg.Button("Stack")],
                    [sg.Button("Queue")],
                    [sg.Button("Exit")]
                ]

        window = sg.Window("Data Structure Visualization", layout, size=(500,500), element_padding=5, margins=(0,150),button_color="orange", element_justification="center")

        while True:
            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Binary Search Tree":
                self.openBSTWindow()
            if event == "Stack":
                self.openStackWindow()
            if event == "Queue":
                self.openQueueWindow()

        window.close()

    def openBSTWindow(self):
        myBSTWindow = bstw.BSTWindow()

    def openStackWindow(self):
        myStackWindow = sw.StackWindow()

    def openQueueWindow(self):
        myQueueWindow = qw.QueueWindow()