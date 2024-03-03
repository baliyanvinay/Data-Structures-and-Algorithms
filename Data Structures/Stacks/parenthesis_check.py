"""
check if the sequence of parenthesis is balanced
"""

from Stack import Stack

input_1 = "[()]{}{[()()]()}"
input_2 = "[(])"

bracket_mapping = {
    "]": "[",
    "}": "{",
    ")": "(",
}

def check_balance(input_str):
    stack = Stack()
    for item in input_str:
        if item in bracket_mapping.values():
            stack.push(item)
        else:
            last_item = stack.pop()
            if last_item != bracket_mapping[item]:
                return False
        
    return True
