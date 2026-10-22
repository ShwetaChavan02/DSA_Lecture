# write a function to swap fisrt and last node in a doubly linaer linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete(self, value):
        temp = self.head

        # Check if list is empty
        if temp is None:
            print("List is empty")
            return

        # Search for the node
        while temp is not None and temp.data != value:
            temp = temp.next

        # Value not found
        if temp is None:
            print("Value is not present in the list")
            return

        # Delete the first node
        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        # Update previous pointer of next node
        if temp.next is not None:
            temp.next.prev = temp.prev

        temp = None
        print("Node deleted successfully")

    def print(self):
        temp = self.head
        print("List Elements:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def count_occ(self, num):
        temp=self.head
        cnt=0
        while temp:
            if temp.data==num:
                cnt+=1
            temp=temp.next
        print("The occurance of the number is :",cnt)

    def swap(self):
        temp=node1=self.head # node1 is firsrt node
        while temp.next: # temp is last node
            temp=temp.next
        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp
    

list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.append(Node(78))

list1.print()

list1.delete(102)
list1.print()
list1.swap()
list1.print()
#list1.count_occ(12)

