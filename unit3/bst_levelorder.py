#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        
       
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
                        
                        
    def delete(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.delete(rt.left, val)
        elif val>rt.data:
            rt.right=self.delete(rt.right, val)
        else:
            if rt.left is None:# node with right child only
                return rt.right
            if rt.right is None:#node with left child only
                return rt.left
            #node has both left and right children
            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.delete(rt.right, succ.data)
        return rt
        
    def get_successor(self,temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp
    
    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False     
            
    def inorder(self, rt):# gives value in ascending/sorted
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is not None or rt.right is not None:
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
            
    def levelorder(self,rt):
            if rt is None:
                print("BST is empty")
                return
            arr=[]
            cnt=0 # for counting visited node
            level=0
            arr.append(rt)
            while cnt<len(arr):
                nodecnt=len(arr)-cnt # no of nodes to be visited
                print("\n Level",level,"nodes:",end=" ")
                for i in range(nodecnt):
                    temp=arr[cnt]
                    cnt+=1
                    print(temp.data, end=" ")
                    if temp.left:
                        arr.append(temp.left)
                    if temp.right:
                       arr.append(temp.right)
                level+=1       
            print("\nHeight of the tree:",level-1)
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
print("\nPreorder: ")
b1.preorder(b1.root)
print("\nPostorder: ")
b1.postorder(b1.root)
#b1.findminmax()
print("\nLevel order")
b1.levelorder(b1.root)

#b1.delete(b1.root,4)
#print("\n After deletion:",end=" ")
#b1.inorder(b1.root)
#if b1.search(4500):
#    print("\n Found the node")
#else:
#    print("\n Not Found")