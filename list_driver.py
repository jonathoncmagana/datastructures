from linked_list import LinkedList, Node
def main():
    print("Linked List driver!")

    my_linked_list = LinkedList() # creates an empty linked list, size 0, and head points to None

    my_linked_list.add(Node("first"))

    my_linked_list.add(Node("second"))

    print(my_linked_list)

    my_linked_list.add(Node("third"))

    print(my_linked_list)





if __name__ == "__main__":
    main()
