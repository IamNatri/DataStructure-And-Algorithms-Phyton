import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def showNode(self):
        return print(self.value)
    

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __empity(self):
        return self.head == None
        

    def insertBegining(self, value):
        new =  Node(value)
        if self.__empity():
            self.tail = new
        new.next = self.head
        self.head = new

    def insertEnd(self, value):
        new = Node(value)
        if self.__empity():
            self.head = new
        else:
            self.tail.next = new
            self.tail = new


    def  listprint (self):
        printval  = self.head
        while printval is not None:
            printval.showNode()
            printval = printval.next
    
    def deletBegining(self):
        
        if self.__empity():
            print('No Data')
            return None
        
        temp = self.head
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return temp
    
    def seach(self, value):
        if self.__empity():
            print('No Data')
            return None
                
        val = self.head
        while val.value is not value:
            if val.next == None:
                return print('Value not Found')
            else:
                val = val.next
            return val

    def deletAt(self, value):
        if self.head == None:
            print('No Data')
            return None
                
        actValue = self.head
        previous = self.head
        while actValue.value is not value:
            if actValue == None:
                return None
            else:
                previous = actValue
                actValue  = actValue.next
        if actValue == self.head:
            self.deletBegining()
        elif actValue == self.tail:
            self.tail = previous
        else:
            previous.next = actValue.next











