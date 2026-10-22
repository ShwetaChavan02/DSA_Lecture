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
        