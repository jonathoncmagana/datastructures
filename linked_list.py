# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Linked List
    def __init__(self, data):  # Constructor
        self.data = data  # The data object for this Node
        self.next = None  # Reference to next Node

    def __str__(self):
        return str(self.data)


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

    # what's big O time add itself is O(n) (linear time)
    # TODO can re-write add, and other functions, so that only data comes in, not a Node
    # TODO Can re-write add so it DOESn't have a loop?
    def add(self, other: Node): #add to end
        cur = self.__head
        steps = 1  # we count 1 step for coming in a function at all
        if (self.size ==0): # empty list coming in to add
            self.__head = other
        else:
            while (cur.next is not None):
                    cur = cur.next
                    steps += 1  # we could each time a loop runs (based on "n" - the number of things in the list)
            cur.next = other
        self.size += 1 # we added one Node
        # print (f"steps for add: {steps}, related to \"n\", the number of items in the list")


    # big O of get? Assume worse case scenario! O(n) linear
    def get(self, index:int): # where head is index 0, head->next would be index 1, etc.
        # we could improve this code by checking for a valid index
        cur = self.__head
        steps = 1
        for i in range(index):
            cur = cur.next
            steps += 1
        # print(f"steps for get: {steps}, related to index we are getting")
        return cur
        # return a Node at index


    def addAt(self, index: int, other:Node):

        # what if we addAt(0)?
        # TODO we need to update the __head!!!!

        # it is inefficient to call get twice, can we only call it once?
        nodeiminus1 = self.get(index-1) # big O(n)
        nodei = self.get(index) # big O(n)
        # TODO how to re-write to call get only once

        # big O(2n), but so what, this is just O(n)

        # we identified 2 operations we needed from our picture:
        nodeiminus1.next = other
        other.next = nodei

    # remove

    # TODO before Thurs: code
    def remove(self, index:int):
        # see picture from video
        # (i-1).next = (i.next)
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
                message += f"{str(cur.data)} -> " # add the current node's data on to the message
                cur = cur.next
            message += str(cur.data)  # add the last node's data to the message
        return message
