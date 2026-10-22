# stack implementation using linked list

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        top=new_node
    def print(self):
        if self.isempty():
            print("Stack is empty...")
        else:
            print("Stack contains...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
