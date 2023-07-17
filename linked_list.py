# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Linked List
    def __init__(self, data, next=None):  # Constructor
        self.data = data  # The data object for this Node
        self.next = next  # Reference to next Node



class LinkedList(object):  # A linked list of data elements
    # class variable to keep track of how many Nodes in list

    def __init__(self):  # Constructor
        self.__head = None  # Reference to start of the Linked List
        self.size = 0

    def isEmpty(self):  # Test for empty list
        return (self.size == 0)
        # return self.__head is None  # True if & only if no 1st Node

    def __len__(self):
        return self.size

    # add
    def add(self, other: Node): #add to end
        cur = self.__head

        if (self.size ==0):
            self.__head = other
        else:
            while (cur.next is not None):
                    cur = cur.next
            cur.next = other
        self.size += 1


    def get(self, index:int):
        pass
    def addAt(self, index: int, other:Node):
        pass
    # remove
    def remove(self, index:int):
        pass
    # print
    def __str__(self):
        return f"{self.__head.data} -> {self.__head.next.data}"