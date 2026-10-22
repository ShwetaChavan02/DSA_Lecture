# singly circular linked list
# append, insert, delete, print
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append a node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Insert a node at a given position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                self.head = new_node
                temp.next = self.head
        else:
            temp = self.head
            count = 1

            if temp is None:
                print("Invalid position")
                return

            while count < pos - 1 and temp.next != self.head:
                temp = temp.next
                count += 1

            if count == pos - 1:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("Invalid position")

    # Delete a node from a given position
    def delete(self, pos):
        if self.head is None or pos < 1:
            print("Invalid position or empty list")
            return

        if pos == 1:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next

                self.head = self.head.next
                temp.next = self.head
        else:
            temp = self.head
            count = 1

            while count < pos - 1 and temp.next != self.head:
                temp = temp.next
                count += 1

            if count == pos - 1 and temp.next != self.head:
                temp.next = temp.next.next
            else:
                print("Invalid position")

    # Print the linked list
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main program
ll = LinkedList()

ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))

print("Original list:")
ll.print_list()

ll.insert(Node(15), 2)
print("After insertion:")
ll.print_list()

ll.delete(3)
print("After deletion:")
ll.print_list()