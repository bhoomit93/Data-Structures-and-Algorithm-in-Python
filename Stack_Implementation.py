"""

@author: Bhoomit Patel

"""

class Stack:

    #Constructor creates a list
    def __init__(self):
        self.stack = []

    #Function to add data to stack. The size is increased by 1
    def push(self,data):
        self.stack.append(data)
        print(data,"pushed to stack")

    #Removes last element from the stack
    def pop(self):
        if len(self.stack) <= 0:
            return ("Stack is Empty!!")
        print(self.stack[len(self.stack)-1], "Popped from the stack")
        return self.stack.pop()

    #Returns true is stack is empty
    def isEmpty(self):
        if len(self.stack) ==0:
            print("The stack is Empty")
            return True
        print("The stack is not Empty")
        return False

    #Returns size of the stack
    def size(self):
        return print("The size of the stack is",len(self.stack))

    def printStack(self):
        print(self.stack)

# Driver program to test the above functions
myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)

myStack.printStack()

myStack.pop()

myStack.printStack()

myStack.isEmpty()
myStack.size()

"""
The output to above Driver program
1 pushed to stack
2 pushed to stack
3 pushed to stack
4 pushed to stack
5 pushed to stack
[1, 2, 3, 4, 5]
5 Popped from the stack
[1, 2, 3, 4]
The stack is not Empty
The size of the stack is 4
"""