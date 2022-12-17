import PySimpleGUI as sg
import Queue

class QueueWindow:

    def __init__(self):
        self.queue = Queue.Queue()

        sg.theme("LightGreen4")

        layout = [
            [sg.Text("Queue")],
            [sg.Text("Enqueue: "), sg.In(size=(5, 1), enable_events=True, key="-ENQUEUEVALUE-"), sg.Button("Enqueue")],
            [sg.Text("Dequeue:"), sg.Button("Dequeue")],
            [sg.Button("Exit")],
            [sg.Graph(canvas_size=(250,250), graph_bottom_left=(0,0), graph_top_right=((250,250)), background_color='CadetBlue2', key='-QUEUEGRAPH-')]
        ]

        window = sg.Window("Queue", layout, size=(400, 400), margins=(0,10), element_justification="center").finalize()

        while True:
            self.drawQueue(window)
            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "Enqueue":
                if values['-ENQUEUEVALUE-'].isnumeric():
                    self.queue.enqueue(values['-ENQUEUEVALUE-'])
                    self.drawQueue(window)
                window['-ENQUEUEVALUE-'].update("")

            elif event == "Dequeue":
                self.queue.dequeue()
                self.drawQueue(window)

        window.close()

    def drawQueue(self, window):

        window['-QUEUEGRAPH-'].erase()

        window['-QUEUEGRAPH-'].draw_line(point_to=(20, 105), point_from=(230, 105), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(20, 145), point_from=(230, 145), color='black', width=3)

        window['-QUEUEGRAPH-'].draw_line(point_to=(45, 105), point_from=(45, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(65, 105), point_from=(65, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(85, 105), point_from=(85, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(105, 105), point_from=(105, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(125, 105), point_from=(125, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(145, 105), point_from=(145, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(165, 105), point_from=(165, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(185, 105), point_from=(185, 145), color='black', width=3)
        window['-QUEUEGRAPH-'].draw_line(point_to=(205, 105), point_from=(205, 145), color='black', width=3)

        x = 55
        for element in self.queue.values:
            window['-QUEUEGRAPH-'].draw_text(text=element, location=(x, 125))
            x += 20