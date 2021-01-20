# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:25:50 2020

@author: 1037624
"""

# Implementation of Queue class
class Queue(object):
    def __init__(self):
        self.items=[] # queue representation using a list
        
    def enqueue(self, data):
        # to add data at the rear of queue
        self.items.append(data)
        
    def dequeue(self):
        # removal of element from front of queue
        self.items.pop(0) # element at zero index
        
    def __str__(self):
        return str(self.items)
    
#________________________________________________________________________________________#

Q1= Queue()
Q1.enqueue(12)
Q1.enqueue(15)
print(Q1)

Q1.dequeue()
print(Q1)
