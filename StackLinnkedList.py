
class Node:
    """create node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class LinkedList:
    """create Linked List class"""
    def __init__(self):
        self.head = None 

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if not self.LinkedList.head:
            return True
        else:
            return False 


if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
