class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def append(self, value):
        new_node = Node(value)  # Create a new node

        if not self.head:  # If the list is empty
            self.head = new_node
            return

        current = self.head
        while current.next is not None:  # Traverse to the end of the list
            current = current.next

        current.next = new_node


    def remove(self, value):
        if self.head is None:  # Check if the list is empty
            return

        if self.head.value == value:
            self.head = self.head.next  # Move head to the next node
            return

        current = self.head
        previous = None

        while current is not None:
            if current.value == value:
                previous.next = current.next
                return
            previous = current
            current = current.next


    def printList(self):

            current = self.head
            while current.next is not None:
                print(current.value)
                current = current.next

            print(current.value)
