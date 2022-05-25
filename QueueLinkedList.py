


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return str(result)

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        return str(self.linkedList)

    def enqueue(self, data):
        node = Node(data)
        if not self.linkedList.head:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    def isEmpty(self):
        if not self.linkedList.head:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty():
            return print("no node is queue")
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None 
            else:
                self.linkedList.head = self.linkedList.head.next
            return print(tempNode)

    def peek(self):
        if self.isEmpty():
            return print("no node is queue")
        else:
            return print(self.linkedList.head)

    def delete(self):
        self.linkedList.head = None 
        self.linkedList.tail = None
        return print('Queue has been deleted')

if __name__ == "__main__":

    que = Queue()
    print(que.isEmpty())
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.peek()
    que.enqueue(4)
    que.enqueue(5)
    print(que.isEmpty())
    print(que)
    que.dequeue()
    print(que)
    que.peek()