# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:55:41 2020

@author: 1037624
"""

# Implementation of Deque
class Deque(object):
    def __init__(self):
        self.items=[] # representation of deque with a list
    
    def add_front(self, data):
        # to add an element at the front of deque
        self.items.append(data)
        
    def add_rear(self, data):
        # to add an element at the front of deque
        self.items.insert(0, data)
        
    def remove_front(self):
        # remove element from front of deque
        self.items.pop()
        
    def remove_rear(self):
        # remove an element from the rear of deque
        self.items.pop(0)
    
    def is_empty(self):
        # return bool if deque is empty 
        return len(self.items)==0
        
    def len_deque(self):
        # returns the length of deque
        return len(self.items)
        
    def __str__(self):
        return str(self.items)

#________________________________________________________________________________________#
D1=Deque()
D1.add_front(12)
D1.add_front(15)

D1.add_rear(10)
D1.add_rear(8)

print(D1)

print(D1.is_empty())
print(D1.len_deque())

D1.remove_front()
D1.remove_rear()

print(D1)
    