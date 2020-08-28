# Implementation of Binary Tree :: 22-Aug-2020
from binarytree import tree

class Node(object):
    def __init__(self, data): # a node in BT would have left and right child
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree(object):
    def __init__(self):
        self.root=None # root will hold the topmost root node
    
    def add_node(self, data):
        new_node=Node(data)
        if not self.root:
            self.root=new_node
        else:
            # in else we have to check where the new_node needs to be inserted
            temp_root=self.root # for traversing
            while(temp_root):
                if new_node.data<temp_root.data: 
                    # if new node is smaller than root node, then left has to be checked
                    temp_root=temp_root.left
                elif new_node.data>temp_root.data:
                    # when new node is greater than root node, then right has to be checked
                    temp_root=temp_root.left
                else:
                    pass # means node already exists and no need to add the node
            # temp_root will now point to an empty left or right, we can add a node here
            temp_root=new_node
    
    def display_node(self):
        pass
        
