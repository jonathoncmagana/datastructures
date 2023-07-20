from linked_list import LinkedList, Node
from timeit import default_timer as timer
def main():
    print("Linked List driver!")

    my_linked_list = LinkedList() # creates an empty linked list, size 0, and head points to None
    """
    #my_linked_list.add(Node("first"))
    for i in range(10):
        my_linked_list.add(Node(i))

    my_linked_list.add(Node("hello mom"))
    print(my_linked_list)

    my_linked_list.addAt(4, Node("I am the new four"))
    print(my_linked_list)
    print(f"test out get(4): {my_linked_list.get(8)}")

    # my_linked_list2 = LinkedList()
    # print(f"test out get(0): {my_linked_list2.get(0)}")


    
    start = timer()
    # we are timing the code between start and end
    my_linked_list.add(Node("second"))
    end = timer()
    print(f"time to add \"second\": {end - start}")  # Time in seconds, e.g. 5.38091952400282

    my_linked_list.add(Node("third"))

    # print(my_linked_list)

    """
    start = timer()
    # we are timing the code between start and end
    for i in range(200): # when you double this number, the time more than doubles. why? O(n^2)
        my_linked_list.add(Node(i))
    end = timer()
    print(f"time to add numbers: {end - start} seconds")  # Time in seconds, e.g. 5.38091952400282
    # my_linked_list.get(89)
    # print(my_linked_list)

    steps = 1
    for i in range(200):  # heres an n
        for j in range(200): # heres an n
            for k in range(200): # heres an n
                steps += 1
    # the whole thing is O(n^3)
    print (steps)

if __name__ == "__main__":
    main()
