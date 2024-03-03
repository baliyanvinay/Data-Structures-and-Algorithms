

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peep(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)
