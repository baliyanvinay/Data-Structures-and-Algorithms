# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 09:26:49 2020

@author: 1037624
"""

# Data Structure Linked List
"""
We need to create a linked_list class where elements are nodes, so we would need two classes
a linked_list class to manage linked_lists and
a node class to manage the properties of a node
"""

# Node class 
class Node():
    def __init__(self, data): # when the node class is called, data will be passed along
        self.data=data
        self.next_node=None
#_________________________________________________________________________________________________#

# linked list class
class Linked_list():
    def __init__(self):
        self.head=None # linked list will have a head pointing to the first element in the sequence
    
    def add_node(self, data):
        # step1: create a new node
        new_node=Node(data) # Node object needs a data variable
        
        # step2: check if head is None. If yes then this is the first element for the linked_list
        # Else means head is not None and the first element already exists
        if self.head is None:
            self.head=new_node # head has been assigned a node
        else:
            # we have to check in else part the node where next_node is None
            last=self.head # to reach to the last element
            while(last.next_node is not None):
                last=last.next_node
            # out of this loop, we will have head pointing to the node where next_node is None
            last.next_node=new_node # last element will point to this new node           
    
    def remove_node(self): # remove last element of linked list
        # step1: traverse to the last element
        last=self.head
        while(last.next_node.next_node): # checking if the next_node of next_node is not None
            last=last.next_node
        last.next_node=None # unlinking/erasing the very last node 
    
    def display_linked_list(self):
        # to display linked_list in a structured way
        print_head=self.head # to preserve the position of head
        while(print_head): # means print_head is not None
            print(print_head.data)
            print_head=print_head.next_node
            
    def add_node_head(self, data):
        # to insert a new node at the begining of linked_list or at head position
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
        
    def remove_node_head(self):
        # to remove node from head and make second element head
        self.head=self.head.next_node
        
    def insert_node(self, data, loc):
        # insert node at a given position in linked_list, i.e., loc
        new_node=Node(data)
        
        # step1: getting index or head to the loc 
        index, loc_head=0, self.head
        while(index!=loc):
            loc_head=loc_head.next_node
            index+=1
        # step2: insert the new_node at loc_head; save loc_head.next_node in new_node.next_node
        new_node.next_node=loc_head.next_node
        loc_head.next_node=new_node
        
    def delete_node(self, loc):
        # remove node from a specific location
        # step1: reaching the location
        index, loc_head=0, self.head
        while(index<loc):
            loc_head=loc_head.next_node
            index+=1
            
        # step2: remove the element by changing the next_node of current location head
        temp=loc_head.next_node.next_node
        loc_head.next_node=None
        loc_head=temp
        
        
#_________________________________________________________________________________________________#

# main program
L1=Linked_list() # instance of linked list
L1.add_node(12)
L1.add_node(15)
L1.add_node_head(10)
L1.add_node_head(5)

print(L1.display_linked_list())
L1.remove_node_head()
print(L1.display_linked_list())

L1.insert_node(14,1)
print(L1.display_linked_list())

L1.delete_node(0)
print(L1.display_linked_list())