import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
    def showNode(self):
        return print(self.value)
    

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __empity(self):
        return self.head == None
        

    def insertBegining(self, value):
        new =  Node(value)
        if self.__empity():
            self.tail = new
        else:
            self.head.previous = new
        new.next = self.head
        self.head = new

    def insertEnd(self, value):
        new = Node(value)
        if self.__empity():
            self.head = new
        else:
            self.tail.next = new
            new.previous = self.tail
        self.tail = new 


    def printAscending  (self):
        printval  = self.head
        while printval is not None:
            printval.showNode()
            printval = printval.next
    
    def printDescending (self):
        printval  = self.tail
        while printval is not None:
            printval.showNode()
            printval = printval.previous
    

    
    def deletBegining(self):
        if self.__empity():
            print('No Data')
            return None
        
        temp = self.head
        if self.head.next == None:
            self.tail = None
        else:
            self.head.next.previous = None   
        self.head = self.head.next
        return temp
    

    def deletEnd(self):
        if self.__empity():
            print('No Data')
            return None
        
        temp = self.tail
        if self.head.next == None:
            self.head = None
        else:
            self.tail.previous.next = None   
        self.tail = self.tail.previous
        return temp


    
    def seach(self, value):
        if self.__empity():
            print('No Data')
            return None
                
        val = self.head
        while val.value != value:
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
        while actValue.value != value:
            actValue = actValue.next
            if actValue == None:
                return None
            
        if actValue == self.head:
            self.head = actValue.next
        else:
            actValue.previous.next = actValue.next
            
        
        if actValue == self.tail:
            self.tail = actValue.next
        else:
            actValue.next.previous = actValue.previous            











