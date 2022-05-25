
class stackLim:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        return str(self.list)

    def isEmpty(self):
        """check list to see if it is empty, return True if so, False otherwise"""
        if self.list == []:
            return print('True')
        else:
            return print('False')

    def isFull(self):
        """is stack full - has it reached its limit"""
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        """push in to stack """
        if self.isFull():
            return print('Cannot push to stack as stack is full')
        else:
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
    stack = stackLim(5)        
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(4)
    stack.push(4)
    stack.push(4)
    print(stack.isFull())
    print(stack)