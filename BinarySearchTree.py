import Queue

class BinarySearchTree():

    def __init__(self, data=None):
        self.data = data
        self.rightChild = None
        self.leftChild = None
        self.parent = None

    def insert(self, value):

        if self.data == None:
            self.data = value #super(BinarySearchTree, self).__init__(value)

        elif value == self.data:
            return

        elif value > self.data:
            if self.rightChild == None:
                self.rightChild = BinarySearchTree(value)
                self.rightChild.parent = self
            else:
                self.rightChild.insert(value)

        else:
            if self.leftChild == None:
                self.leftChild = BinarySearchTree(value)
                self.leftChild.parent = self
            else:
                self.leftChild.insert(value)

    def minValueNode(self):
        current = self
        # loop down to find the leftmost leaf
        while (current.leftChild is not None):
            current = current.leftChild
        return current

    def maxValueNode(self):
        current = self
        # loop down to find the leftmost leaf
        while (current.rightChild is not None):
            current = current.rightChild

        return current

    def mostMiddleNode(self): #finds the smallest node in the right subtree (one of two middle nodes)
        return self.rightChild.minValueNode()

    def printTree(self):

        if self.rightChild == None and self.leftChild == None:
            print("data:", self.data, "\nright child:", self.rightChild, "\nleft child:", self.leftChild)

        elif self.leftChild == None:
            print("data:", self.data, "\nright child:")
            self.rightChild.printTree()
            print("left child:", self.leftChild)

        elif self.rightChild == None:
            print("data:", self.data)
            print("right child:", self.rightChild, "\nleft child:")
            self.leftChild.printTree()

        else:
            print("data:", self.data)
            print("right child:", )
            self.rightChild.printTree()
            print("left child:")
            self.leftChild.printTree()

    def inOrderPrint(self):
        if self.leftChild:
            self.leftChild.inOrderPrint()
        print(self.data, end=" ")
        if self.rightChild:
            self.rightChild.inOrderPrint()

    def formattedInOrderPrint(self):
        print("[ ", end="")
        self.inOrderPrint()
        print("]")

    def find(self, value):
        if self.data is None:
            print(str(value) + " Not Found")
            return
        if value < self.data:
            if self.leftChild is None:
                print(str(value) + " Not Found")
                return
            return self.leftChild.find(value)
        elif value > self.data:
            if self.rightChild is None:
                print(str(value) + " Not Found")
                return
            return self.rightChild.find(value)
        else:
            return self

    def delete(self, value):

        if not self.find(value): #case where the value is not in the tree
            print("Error: value not in tree")
            return

        #error checking is done, next is deletion code

        elif value < self.data: #if value is left of node, call delete on the left subtree
            self.leftChild.delete(value)

        elif value > self.data: #if value is right of node, call delete on the right subtree
            self.rightChild.delete(value)

        else: #case where data of current node equals value, start deleting

            if self.leftChild is None: #note works if node has 0 or 1 children

                if self.rightChild is not None:
                    if self.parent:
                        self.rightChild.parent = self.parent
                        if self.parent.rightChild is self:
                            self.parent.rightChild = self.rightChild
                        else:
                            self.parent.leftChild = self.rightChild
                    else:
                        temp = self.rightChild.data
                        self.delete(self.rightChild.data)
                        self.data = temp
                else:
                    if self.parent:
                        if self.parent.rightChild is self:
                            self.parent.rightChild = None
                        else:
                            self.parent.leftChild = None
                    else:
                        self.data = None

            elif self.rightChild is None:

                if self.leftChild is not None:
                    if self.parent:
                        self.leftChild.parent = self.parent
                        if self.parent.leftChild is self:
                            self.parent.leftChild = self.leftChild
                        else:
                            self.parent.rightChild = self.leftChild
                    else:
                        temp = self.leftChild.data
                        self.delete(self.leftChild.data)
                        self.data = temp
                else:
                   if self.parent:
                        if self.parent.leftChild is self:
                            self.parent.rightChild = None
                        else:
                            self.parent.rightChild = None
                   else:
                       self.data = None

            else: #case with 2 children
                temp = self.mostMiddleNode().data
                self.delete(self.mostMiddleNode().data)
                self.data = temp

    def breadthFirstList(self): #returns the binary tree as a breadth first (level by level list)
        BFList = []
        if self.data is None:
            return
        BFQueue = [self]

        while BFQueue:
            node = BFQueue.pop(0)
            #print(node.data, end=" ")
            BFList.append(node.data)
            if node.leftChild:
                BFQueue.append(node.leftChild)
            if node.rightChild:
                BFQueue.append(node.rightChild)

        return BFList

    def completeBFList(self):
        completeList = []

        for node in range(pow(2,self.height()) - 1):
            completeList.append(None)

        completeList[0] = self.data

        for i in range(int(pow(2,self.height()) / 2) - 1):  #loops through all elements not in the bottom level of the tree

            if completeList[i] is not None:
                if self.find(completeList[i]).rightChild and self.find(completeList[i]).leftChild:
                    completeList[2 * (i + 1) - 1] = self.find(completeList[i]).leftChild.data
                    completeList[2 * (i + 1)] = self.find(completeList[i]).rightChild.data

                elif self.find(completeList[i]).leftChild:
                    completeList[2 * (i + 1) - 1] = self.find(completeList[i]).leftChild.data

                elif self.find(completeList[i]).rightChild:
                    completeList[2 * (i + 1)] = self.find(completeList[i]).rightChild.data

        return completeList

    def height(self):
        if self.data is None or self is None:
            return 0

        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.height(), self.rightChild.height())
        elif self.leftChild:
            return 1 + self.leftChild.height()
        elif self.rightChild:
            return 1 + self.rightChild.height()
        else:
            return 1

    def findLevel(self,value):
        level = 0
        counter = 1
        for i in range(len(self.completeBFList())):
            if self.completeBFList()[i] == value:
                return level

            if pow(2,level) == counter:
                level += 1
                counter = 0
            counter += 1