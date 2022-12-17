class Stack:

    def __init__(self):
        self.values = [] #the stack will add and remove values to/from the end of the list

    def pop(self):
        if not self.isEmpty():
            return self.values.pop(-1)
        else:
            print("Error: Stack is empty")

    def push(self, value):
        if self.size() < 9:
            self.values.append(value)
        else:
            print("Error: max stack size reached")

    def peek(self):
        if not self.isEmpty():
            return self.values[-1]
        else:
            print("Error: Stack is empty")

    def isEmpty(self):
        if self.values:
            return False
        else:
            return True

    def size(self):
        return len(self.values)

    def printStack(self):
        print(self.values)