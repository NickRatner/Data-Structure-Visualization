import PySimpleGUI as sg
import Stack

class StackWindow:

    def __init__(self):
        self.stack = Stack.Stack()

        sg.theme("LightGreen4")

        layout = [
            [sg.Text("Stack")],
            [sg.Text("Push: "), sg.In(size=(5, 1), enable_events=True, key="-PUSHVALUE-"), sg.Button("Push")],
            [sg.Text("Pop:"), sg.Button("Pop")],
            [sg.Button("Exit")],
            [sg.Graph(canvas_size=(250,250), graph_bottom_left=(0,0), graph_top_right=((250,250)), background_color='CadetBlue2', key='-STACKGRAPH-')]
        ]

        window = sg.Window("Stack", layout, size=(400, 400), margins=(0,10), element_justification="center").finalize()

        while True:
            self.drawStack(window)
            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "Push":
                if values['-PUSHVALUE-'].isnumeric():
                    self.stack.push(values['-PUSHVALUE-'])
                    self.drawStack(window)
                window["-PUSHVALUE-"].update("")


            elif event == "Pop":
                self.stack.pop()
                self.drawStack(window)

        window.close()

    def drawStack(self, window):

        window['-STACKGRAPH-'].erase()

        window['-STACKGRAPH-'].draw_line(point_to=(95,20), point_from=(95,200), color='black', width=3)
        window['-STACKGRAPH-'].draw_line(point_to=(155, 20), point_from=(155, 200), color='black', width=3)
        window['-STACKGRAPH-'].draw_line(point_to=(94, 20), point_from=(157, 20), color='black', width=3)

        y = 40
        for element in self.stack.values:
            window['-STACKGRAPH-'].draw_line(point_to=(94, y), point_from=(157, y), color='black', width=3)
            window['-STACKGRAPH-'].draw_text(text= element,location=(125,y-10))
            y += 20


