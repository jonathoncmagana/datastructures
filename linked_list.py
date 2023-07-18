# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Linked List
    def __init__(self, data):  # Constructor
        self.data = data  # The data object for this Node
        self.next = None  # Reference to next Node



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
    # assumptions for functions:
    # 1. assume we have a valid Linked List that we are adding to
    # 2. make sure all linked list parameters are updated in the function
    # 3. at end of function, make sure we have a valid linked
    def add(self, other: Node): #add to end
        cur = self.__head

        if (self.size ==0): # empty list coming in to add
            self.__head = other
        else:
            while (cur.next is not None):
                    cur = cur.next
            cur.next = other
        self.size += 1 # we added one Node


    # TODO before Weds: code get
    def get(self, index:int): # where head is index 0, head->next would be index 1, etc.
        pass
        # return a Node at index

    # TODO before Weds: code or psuedocode
    def addAt(self, index: int, other:Node):
        pass
    # remove

    # TODO before Weds: code or psuedocode
    def remove(self, index:int):
        pass
    # print
    # assmume we have a valid list coming in
    # this should be a "read only" function
    def __str__(self):
        cur = self.__head
        message = ""
        if (self.size == 0):  # empty list coming in
            return "empty linked list"
        else:  # we don't have an empty list
            while (cur.next is not None):
                message += cur.data + " -> " # add the current node's data on to the message
                cur = cur.next
            message += cur.data # add the last node's data to the message
        return message
