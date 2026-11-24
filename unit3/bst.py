# Binary search Tree Implementation in Python

class Node:
    def __init__(self, value):
        self.left = None
        self.data=value
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None # innitialization of tree

    # inserting a node in tree 
    def insert(self,new_node):
        if self.root is None: # root is None, then new node will be root
            self.root = new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node # new node will be inserted as left child of temp
                        return
                    else:
                        temp=temp.left # traversing the left subtree of temp
                else:
                    if temp.right is None:
                        temp.right=new_node # new node will be inserted as right child of temp
                        return
                    else:
                        temp=temp.right # traversing the right subtree of temp

def inorder(temp): #recursive function to perform inorder traversal of tree
    if temp is None:
        return        
    else:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right) 

btree=BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))
inorder(btree.root)
