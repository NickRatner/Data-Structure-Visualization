import PySimpleGUI as sg
import BinarySearchTree as BST

class BSTWindow:

    def __init__(self):
        self.bst = BST.BinarySearchTree()

        sg.theme("LightGreen4")

        layout = [
            [sg.Text("Binary Search Tree")],
            [sg.Text("Insert: "), sg.In(size=(5, 1), enable_events=True, key="-INSERTVALUE-"), sg.Button("Insert")],
            [sg.Text("Delete:"), sg.In(size=(5, 1), enable_events=True, key="-DELETEVALUE-"), sg.Button("Delete")],
            [sg.Button("Exit")],
            [sg.Graph(canvas_size=(250,250), graph_bottom_left=(0,0), graph_top_right=((250,250)), background_color='CadetBlue2', key='-BSTGRAPH-')]
        ]

        window = sg.Window("Binary Search Tree", layout, size=(400, 400), margins=(0,10), element_justification="center")

        while True:
            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "Insert":
                if values['-INSERTVALUE-'].isnumeric():
                    self.bst.insert(int(values['-INSERTVALUE-']))
                    self.drawBST(window)
                window['-INSERTVALUE-'].update("")

            elif event == "Delete":
                if values['-DELETEVALUE-'].isnumeric():
                    self.bst.delete(int(values['-DELETEVALUE-']))
                    self.drawBST(window)
                window['-DELETEVALUE-'].update("")

        window.close()

    def drawBST(self, window):

        window['-BSTGRAPH-'].erase()

        x = 125
        y = 200
        level = 0
        counter = 1
        for node in self.bst.completeBFList():
            if node is not None:
                window['-BSTGRAPH-'].draw_circle(center_location=(x,y), radius=10)
                window['-BSTGRAPH-'].draw_text(text=node, location=(x,y))

                if self.bst.find(node).parent:
                    if self.bst.findLevel(node) == 1:
                        if self.bst.completeBFList()[1] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(118,193),point_to=(117,167), color="black",width=1)
                        elif self.bst.completeBFList()[2] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(132,193), point_to=(133,167), color="black", width=1)

                    elif self.bst.findLevel(node) == 2:
                        if self.bst.completeBFList()[3] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(103,153),point_to=(87,127), color="black",width=1)
                        elif self.bst.completeBFList()[4] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(117,153), point_to=(117,127), color="black", width=1)
                        elif self.bst.completeBFList()[5] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(133,153),point_to=(133,127), color="black",width=1)
                        elif self.bst.completeBFList()[6] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(147,153), point_to=(163,127), color="black", width=1)

                    elif self.bst.findLevel(node) == 3:
                        if self.bst.completeBFList()[7] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(73,113),point_to=(27,87), color="black",width=1)
                        elif self.bst.completeBFList()[8] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(87,113), point_to=(43,87), color="black", width=1)
                        elif self.bst.completeBFList()[9] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(103,113),point_to=(87,87), color="black",width=1)
                        elif self.bst.completeBFList()[10] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(117,113), point_to=(103,87), color="black", width=1)
                        elif self.bst.completeBFList()[11] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(133,113),point_to=(133,87), color="black",width=1)
                        elif self.bst.completeBFList()[12] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(147,113), point_to=(163,87), color="black", width=1)
                        elif self.bst.completeBFList()[13] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(163,113),point_to=(207,87), color="black",width=1)
                        elif self.bst.completeBFList()[14] == node:
                            window['-BSTGRAPH-'].draw_line(point_from=(177,113), point_to=(223,87), color="black", width=1)

            x += 30

            if pow(2,level) == counter:
                y -= 40
                level += 1

                x = 125 - ((pow(2,level) - 1) * 30)/2

                counter = 0
            counter += 1