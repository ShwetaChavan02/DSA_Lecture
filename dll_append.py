# doubly linked list
# append, insert and print function

class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append function
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Insert function
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    # Print function
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))

print("Original list:")
list1.print_list()

list1.insert(Node(25), 2)

print("After insertion:")
list1.print_list()
