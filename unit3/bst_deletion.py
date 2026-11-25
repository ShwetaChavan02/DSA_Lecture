#Binary search tree implementation using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.cnt = 0
    # insertion  
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    # deletion
    def del_node(self, rt, value):
        if rt is None:
            return rt
        if value < rt.data:
            rt.left = self.del_node(rt.left, value)
        elif value > rt.data:
            rt.right = self.del_node(rt.right, value)
        else:
            if rt.left is None: # node with right child only
                return rt.right 
            if rt.right is None: # node with left child only
                return rt.left
            # node has returned both left and right child
            successor = self.get_successor(rt) 
            rt.data = successor.data # deleted nodes data is replaced with successor's data
            rt.right = self.del_node(rt.right, successor.data) # delete the successor node

    def get_successor(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left # traversing the left subtree of temp to find the successor node
        return temp

    # searching a node in BST
    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left # searching in left subtree of temp
            else:
                temp = temp.right # searching in right subtree of temp
        return False

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is not None or rt.right is not None:
                self.cnt+=1
            self.inorder(rt.right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nMin: ", temp.data)
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)


b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(50))
b1.insert(Node(500))
print("\nInorder: ")
b1.inorder(b1.root)
#print("\nNo of nodes: ",b1.cnt)
#print("\nLeaf nodes:",b1.cnt)
#print("\nNon-Leaf nodes:",b1.cnt)
#print("\nPreorder: ")
#b1.preorder(b1.root)
#print("\nPostorder: ")
#b1.postorder(b1.root)
#b1.findminmax()
b1.del_node(b1.root, 4)
print("\nInorder after deletion: ", end=" ")
b1.inorder(b1.root)
if b1.search(4):
    print("\n Node found")
else:
    print("\n Node not found")