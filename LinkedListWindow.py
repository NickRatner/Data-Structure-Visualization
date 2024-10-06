import PySimpleGUI as sg
import LinkedList

class LinkedListWindow:

    def __init__(self):
        self.linkedList = LinkedList.LinkedList()

        sg.theme("LightGreen4")

        layout = [
            [sg.Text("Linked List")],
            [sg.Text("Append: "), sg.In(size=(5, 1), enable_events=True, key="-APPENDVALUE-"), sg.Button("Append")],
            [sg.Text("Remove:"), sg.In(size=(5, 1), enable_events=True, key="-REMOVEVALUE-"), sg.Button("Remove")],
            [sg.Button("Exit")],
            [sg.Graph(canvas_size=(250, 250), graph_bottom_left=(0, 0), graph_top_right=((250, 250)),
                      background_color='CadetBlue2', key='-LINKEDLISTGRAPH-')]
        ]

        window = sg.Window("Linked List", layout, size=(400, 400), margins=(0, 10), element_justification="center").finalize()

        while True:
            self.drawLinkedList(window)

            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "Append":
                if values['-APPENDVALUE-'].isnumeric():
                    self.linkedList.append(int(values['-APPENDVALUE-']))
                    self.drawLinkedList(window)
                window['-APPENDVALUE-'].update("")

            elif event == "Remove":
                if values['-REMOVEVALUE-'].isnumeric():
                    self.linkedList.remove(int(values['-REMOVEVALUE-']))
                    self.drawLinkedList(window)
                window['-REMOVEVALUE-'].update("")

        window.close()


    def drawLinkedList(self, window):
        window['-LINKEDLISTGRAPH-'].erase()

        x = 45
        if self.linkedList.head:
            current = self.linkedList.head
            while current is not None:

                #draw box
                window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x-10, 80), point_from=(x-10, 140), color='black', width=3)
                window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x+10, 80), point_from=(x+10, 140), color='black', width=3)
                window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x-10, 80), point_from=(x+10, 80), color='black', width=3)
                window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x-10, 110), point_from=(x+10, 110), color='black', width=3)
                window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x-10, 140), point_from=(x+10, 140), color='black', width=3)

                # draw value
                window['-LINKEDLISTGRAPH-'].draw_text(text=current.value, location=(x, 125))

                #print arrow to next value
                if current.next is not None:
                    window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x, 95), point_from=(x + 35, 125), color='black', width=3)
                    window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x + 20, 120), point_from=(x + 35, 125), color='black', width=3)
                    window['-LINKEDLISTGRAPH-'].draw_line(point_to=(x + 30, 110), point_from=(x + 35, 125), color='black', width=3)

                x += 45

                current = current.next