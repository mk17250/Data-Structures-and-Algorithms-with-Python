
class Queue:
    """Queue class"""
    def __init__(self, data):
        self.values = [data]
    
    def __str__(self):
        return str(self.values)

    def isEmpty(self):
        if self.values == []:
            return True
        else:
            return False 

    def enqueue(self, data):
        if self.isEmpty():
            return print('List is empty')
        else:
            return self.values.append(data)

    def dequeue(self):
        if self.isEmpty():
            return print('List is empty')
        else:
            self.values.pop(0)

    def peek(self):
        if self.isEmpty():
            return print('List is empty')
        else:
            return print(self.values[0])

    def deleteQueue(self):
        self.values = []
        return print('Queue has been deleted')

    
if __name__ == "__main__":
    queue = Queue(1)
    print(queue.isEmpty())
    # queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    queue.peek()
    print(queue.isEmpty())
    queue.dequeue()
    print(queue)
    queue.peek()
    queue.deleteQueue()
    queue.dequeue()
    queue.enqueue(4)

