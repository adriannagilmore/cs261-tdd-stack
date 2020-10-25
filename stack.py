# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def __init__(self):
        self.myStack = []

    def is_empty(self):
        if len(self.myStack) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            raise IndexError
        else: 
            return self.myStack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.myStack[-1]

    def push(self, item):
        self.myStack.append(item)