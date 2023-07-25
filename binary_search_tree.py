# we inherit from object by convention here (and possibly
# for compatibility with older versions of python).
# It used to be needed in python 2,
# but in python 3 it is no longer needed
class Node(object):  # One part of the data Tree
    def __init__(self, data):  # Constructor
        self.data = data  # The data object for this Node
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
    # Rules for data struct functions:
    # 1. before function is called, we have a valid data structure (BST)
    # 2. update all attributes (root, size, left and right of Nodes)
    # 3. on the way out, the function must leave the data structure valid
    def add(self, dataToAdd): # we decided that adding is log(N) (LOG BASE 2)
        nodeToAdd = Node(dataToAdd) # QoL improvement, hide Nodes from user
        cur = self.__root  # the current Node we are looking at

        self.size += 1
        steps = 1
        if cur is None:  # For empty trees, insert new node at root
            self.__root = nodeToAdd  # root of tree
        else:
            # we at least have a root already
            lookingForSpot = True

            while (lookingForSpot):
                steps +=1
                if dataToAdd < cur.data:  # If new data is less cur's data, go left
                    if (cur.left is None):  # if there is a open spot
                        cur.left = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.left  # equivalent of cur = cur.next in LL. Meaning keeping going
                else:  # Otherwise >= look right
                    if (cur.right is None):
                        cur.right = nodeToAdd
                        lookingForSpot = False
                    else:
                        cur = cur.right  # equivalent of cur = cur.next in LL. Meaning keeping going
            print (f"steps for adding {dataToAdd}: {steps}")


    # TODO find. Excersize for Weds, try to code. return True if it finds it, false if not
    def find(self, dataToFind): # takes data, NOT a Node
        pass

    # TODO print with __str__ is "hard coded", needs to be better
    # TODO can we make it generic, and then, can we use recursion?
    # TODO think about psuedo code for more generic printing. Doesn't have to be pretty
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
