# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:08:16 2020

@author: 1037624
"""
'''
21-Aug-2020 :: Stack data structure implementation in Python
'''
# Stack class
class Stack(object):
    def __init__(self):
        # needs an empty list to represent stack
        self.items=[]
    
    def push(self, data):
        # to add an element on the top of stack
        self.items.append(data)
    
    def pop(self):
        # last added element will be removed
        self.items.pop()
        
    def peep(self):
        # to display the last added element but without removing it
        return self.items[-1]
        
    def is_Empty(self):
        # returns bool for if stack is empty or not
        return len(self.items)==0
    
    def len_stack(self):
        # returns the lenght of stack
        return len(self.items)
#_______________________________________________________________________________________#

S1=Stack()

print(S1.is_Empty())
print(S1.push(12))
print(S1.peep())

print(S1.len_stack())

    