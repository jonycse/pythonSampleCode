class MyStack():
    stack = []
    max_stack_size = 2

    def push(self, value):
        if len(self.stack) == self.max_stack_size:
            return "Overflow"
        self.stack.append(value)
    def pop(self):
        if(len(self.stack)):
            return self.stack.pop()
        return "Underflow"

myStack = MyStack()
myStack.push(2)
myStack.push(5)
print myStack.stack
print myStack.push(6)
print myStack.stack
print myStack.pop()
print myStack.stack
print myStack.pop()
print myStack.pop()
print myStack.stack
