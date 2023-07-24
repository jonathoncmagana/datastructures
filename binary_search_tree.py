# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Linked List
    def __init__(self, data):  # Constructor
        self.data = data  # The data object for this Node
        self.next = None  # Reference to next Node
        self.left = None  # the left child
        self.right = None  # the right child

    def __str__(self):
        return str(self.data)

class BST(object):  # A binary search tree of data elements
    # class variable to keep track of how many Nodes in list

    def __init__(self):  # Constructor
        self.__root = None  # Reference to start of BST
        self.size = 0


    # add (aka insert)
    # this function does NOT keep the tree balanced
    def add(self, dataToAdd):
        nodeToAdd = Node(dataToAdd)
        cur = self.__root

        self.size += 1

        if cur is None:  # For empty trees, insert new node at root
            self.__root = nodeToAdd  # root of tree
        else:

            lookingForSpot = True

            while (lookingForSpot):
                if dataToAdd < cur.data:  # If new data is less cur's data, go left
                    if (cur.left is None):
                        cur.left = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.left
                else:  # Otherwise >= look right
                    if (cur.right is None):
                        cur.right = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.right


    # TODO find
    def find(self, dataToFind): # takes data, NOT a Node
        pass

    # TODO print with __str__ is "hard coded", needs to be better
    # TODO can we make it generic, and then, can we use recursion?
    def __str__(self):
        message = f"\t  {self.__root}\n"

        if (self.size>1):
            message += f"\t/\t\\\n"
            message += f"  {self.__root.left}\t\t  {self.__root.right}\n"

        if (self.size>3):
            message += f"/\t\\\t/\t\\\n"
            message += f"{self.__root.left.left}\t{self.__root.left.right}"
            message += f"\t{self.__root.right.left}\t{self.__root.right.right}"

        return message

    # TODO recursive add

    # TODO recursive find

    # how would delete work?
