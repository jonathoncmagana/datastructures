from binary_search_tree import BST, Node
from timeit import default_timer as timer
def main():
    print("BST driver!")

    mywords = BST()

    mywords.add("mom")
    mywords.add("sister")
    mywords.add("dad")


    #print(mywords)


    my_BST = BST() # creates an empty BST, size 0, and root points to None

    # TODO: Question - the order I add things in matters to how the tree
    # TODO gets structured. Why?
    my_BST.add(4)
    my_BST.add(6)
    my_BST.add(2)
    my_BST.add(1)
    my_BST.add(3)
    my_BST.add(5)
    my_BST.add(7)

    print(my_BST)
    """
    start = timer()
    # we are timing the code between start and end
    for i in range(200): # when you double this number, the time more than doubles. why? O(n^2)
        my_linked_list.add(Node(i))
    end = timer()
    print(f"time to add numbers: {end - start} seconds")  # Time in seconds, e.g. 5.38091952400282
    """
if __name__ == "__main__":
    main()
