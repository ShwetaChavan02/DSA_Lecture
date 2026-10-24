# linear queue using linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

