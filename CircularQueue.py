
from multiprocessing import set_forkserver_preload
from sys import maxsize


class CircularQueue:
    """Create circular queue class"""
    def __init__(self, maxSize):
        self.values = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1 
        self.top = -1 

    def __str__(self):
        return str(self.values)

    def isFull(self):
        """method to check if queue is full"""
        if self.top +1 == self.start:
            return True 
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True 
        else:
            return False 

    def isEmpty(self):
        """method to check if queue is empty"""
        if self.top == -1:
            return True
        else: 
            return False

    def enqueue(self, value):
        """method to add items to end of queue"""
        if self.isFull():
            return print("Queue is FULL - unable to add element")
        else:
            if self.top+1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.values[self.top] = value 
        
    def dequeue(self):
        """method to remove item at start of queue """
        if self.isEmpty():
            return print("There is no element in the Queue")
        else:
            firstElement = self.values[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0 
            else:
                self.start += 1
            self.values[start] = None 
            return firstElement

    def peek(self):
        """method to see first element in Queue"""
        if self.isEmpty():
            return print("There is no element in the Queue")
        else:
            return print(self.values[self.start])

    def deleteQueue(self):
        """"method to delete Queue"""
        self.values = self.maxSize * [None]
        self.start = -1 
        self.top = -1 
        return print('Queue has been deleted')

if __name__ == '__main__':
    que = CircularQueue(5)
    print(que.isEmpty())
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    que.enqueue(1)
    print(que)
    print(que.isEmpty())
    print(que.isFull())
    que.dequeue()
    que.dequeue()
    que.dequeue()
    print(que)
    que.enqueue(99)
    que.enqueue(99)
    print(que)
    print(que.isEmpty())
    que.peek()
    que.dequeue()
    que.dequeue()
    print(que)
    que.peek()
    que.enqueue(10)
    que.enqueue(20)
    que.enqueue(30)
    que.enqueue(30)
    print(que)
    que.peek()
    que.deleteQueue()
    que.peek()