
class Stack:
    """stack class using python list"""
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def isEmpty(self):
        """check list to see if it is empty, return True if so, False otherwise"""
        if self.list == []:
            return print('True')
        else:
            return print('False') 

    def push(self, value):
        """push method"""
        return self.list.append(value)

    def pop(self):
        """method to pop last item from stack"""
        # check to see if stack is empty
        if self.list == []:
            return print('Stack is empty')
        else:
            return print(self.list.pop())

    def peek(self):
        """method to display the top item in stack ready to be accessed"""
        if self.list == []:
            return print('Stack is empty')
        else:
            return print(self.list[-1])

    def deleteStack(self):
        """delete entire stack"""
        self.list = None 
        return self.list

    def printStack(self):
        """print stack"""
        return print(self.list)

if __name__ == '__main__':

    newStack = Stack()
    newStack.isEmpty()
    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    newStack.pop()
    print(newStack)
    newStack.push(3)
    newStack.push(4)
    newStack.push(5)
    newStack.push(6)
    print(newStack)
    newStack.peek()
    newStack.printStack()
    newStack.deleteStack()
    print(newStack)