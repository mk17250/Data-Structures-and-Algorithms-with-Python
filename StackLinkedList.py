
class Node:
    """create node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class LinkedList:
    """create Linked List class"""
    def __init__(self):
        self.head = None 

    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next

        return str(result)

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
        
    def __str__(self):
        return str(self.LinkedList)
        

    def isEmpty(self):
        if not self.LinkedList.head:
            return True
        else:
            return False 

    def push(self, data):
        """create method topush into stack"""
        node = Node(data)
        node.next = self.LinkedList.head
        self.LinkedList.head = node 

    def pop(self):
        """method to pop first element from stack """
        if self.isEmpty():
            return print("Stack is empty")
        else:
            nodeValue = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        """method to pop first element from stack """
        if self.isEmpty():
            return print("Stack is empty")
        else:
            nodeValue = self.LinkedList.head.data
            return print(nodeValue)
    
    def delete(self):
        """method to delete stack"""
        self.LinkedList.head = None 
        return print('Stack has been deleted')


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    print(stack.isEmpty())
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.peek()
    stack.delete()
    stack.pop()