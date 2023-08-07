import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def showNode(self):
        return print(self.value)
    
class StackLinledList:
    def __init__(self):
        #self.__capacity = capacity
        self.head = None
        #self.__values = np.empty(self.__capacity, dtype=int)

    def isEmpty(self):
        return self.head == None

    def push(self, value):
        new = Node(value)
        if self.isEmpty():
            self.head = new
        else:
            new.next = self.head
            self.head = new

        return self.head

    def pop(self):
        if self.isEmpty():
            print('No data in the Stack')
        else:
            self.head = self.head.next

    
    def top(self):
        if self.isEmpty():
            print('No data in the Stack')
        else:
            print(self.head.value)    
            return self.head
    
    def stackPrint(self):
        if self.isEmpty():
            print('No data to print.')
        valuePrint = self.head
        while valuePrint != None:
            print(valuePrint.value)
            valuePrint = valuePrint.next



