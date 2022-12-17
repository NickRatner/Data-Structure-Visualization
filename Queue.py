class Queue:

    def __init__(self):
        self.values = []  # the stack will add and remove values to/from the end of the list

    def enqueue(self, value):
        if self.size() < 9:
            self.values.append(value)
        else:
            print("Error: Max queue size reached")
    def dequeue(self):
        if not self.isEmpty():
            self.values.pop(0)
        else:
            print("Error: Queue is empty")

    def front(self):
        if not self.isEmpty():
            return self.values[0]
        else:
            print("Error: Queue is empty")

    def rear(self):
        if not self.isEmpty():
            return self.values[-1]
        else:
            print("Error: Queue is empty")

    def isEmpty(self):
        if self.values:
            return False
        else:
            return True

    def size(self):
        return len(self.values)

    def printQueue(self):
        print(self.values)