"""reverse a string using stack"""

from stack import Stack

def reverseString(input_str):
    stack = Stack()
    for item in input_str:
        stack.push(item)
    
    res = ""
    while not stack.isEmpty:
        res += stack.pop()
    
    return res
