# Create a Node class, with the attributes. data, next, previous 

class Node:
    """create node class, with the attributes data, next, prev"""
    def __init__(self, data_value=None):
        self.data = data_value
        self.next = None 
        self.prev = None 

# Create a DLL class 
class DoubleLinkedList:
    """create DLL class with the attributes, head and tail"""
    def __init__(self):
        # Note - Tail will be utilised for DLL unlike for SLL/CSLL as this is helpful for reverse traversal/printing
        self.head = None 
        self.tail = None 
        
    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return str(result)


    def createDLL(self, data_value=None):
        """method for DLL creation, must be intialised with a value, or will be set to None value"""
        # create new node with value
        newNode = Node(data_value)
        # set head to new node 
        self.head = newNode
        # set tail to newNode
        self.tail = newNode
        # Note - both the prev/next pointer remain None 

    def insertDLL(self, data_value=None, index='end'):
        """method to insert into DLL at start (0), end ('end, no index parameter passed) and anywhere else"""
        if self.head == None:
            return print('DLL is empty - cannot insert')
        else:
            # create new node and intialise with value 
            newNode = Node(data_value)
            # if index == 0
            if index == 0:
                if not self.head.next:
                    # set prev pointer of existing node to new node
                    self.head.prev = newNode
                    # set tail to node
                    self.tail = self.head
                    # set the pointer of newNode to the exisiting node
                    newNode.next = self.head
                    # set head to newNode
                    self.head = newNode
                else:
                    # set prev pointer of existing node to new node
                    self.head.prev = newNode
                    # set the pointer of newNode to the exisiting node
                    newNode.next = self.head
                    # set head to newNode
                    self.head = newNode
            # if index value is not passed and is therefore = 'end' and therefore we wish to insert at the end of the DLL
            elif index == 'end':
                # check to see if only node in list
                if self.head == self.tail:
                    # if it is, set tail to new node
                    self.tail = newNode
                    # set prev on new node to first node 
                    newNode.prev = self.head
                    # set pointer of first node to new node
                    self.head.next = newNode
                else:
                    # set node = head, which is start of DLL
                    node = self.head
                    # while True or while not empty 
                    while node.next:
                        # move to next node
                        node = node.next
                    # once node.next = None, which is the end of the DLL the loop will break
                    # then set pointer of final node, which is currently = none to newNode
                    node.next = newNode
                    # set prev pointer of newnode to end of DLL
                    newNode.prev = node 
                    # set tail to newNode
                    self.tail = newNode
            else:
                # insert anywhere else in list 
                # set node to start of DLL
                node = self.head
                # set counter for traversl 
                counter = 0
                while counter < index -1:
                        node = node.next
                        if not node.next:
                            return print('Index out of range')
                        else:
                            counter += 1
                # set pointer of new node to next node 
                newNode.next = node.next
                # set pointer of current node to newNode
                node.next = newNode
                # set newNode prev pointer to curreent node
                newNode.prev = node
                # set prev pointer of node past newNode to newNode
                node = node.next.next
                node.prev = newNode
                
    def searchValueDLL(self, value):
        """method to search for value in DLL and return value if in list, return not found if not"""
        # check if DLL is not empty, print statement if empty 
        if not self.head:
            return print("DLL is empty")
        else:
            # else, set node to pointer of DLL
            node = self.head
            # while node is True (not None)
            while node:
                if node.data == value:
                    return print(node.data)
                else:
                    node = node.next
            return print('Value not found in DLL')

    def searchIndex(self, index=0):
        """Method to return value t given index - return 'out of range of DLL' if index out of range"""
        # if DLL is empty print...
        if not self.head:
            return print('DLL is empty')
        else:
        # if position is 0 return data value here
            if index == 0:
                return print(self.head.data)
            else:
                # else, set counter to track traversal through list 
                counter = 0
                # set node to pointer for start of DLL
                node = self.head 
                # while counter less tht index, traverse through list, unless next is none (end of list)
                while counter < index:
                    if not node.next:
                        return print('Index out of range of DLL')
                    else:
                        # if not end of list, traverse and add counter until reaching location of index value, then loop will break
                        node = node.next
                        counter += 1
                # return data vaue of node at index location 
                return print(node.data)

    def deleteNodeOfDLL(self, index='end'):
        """Method to delete node at beginning, end and anywhere else in list - Note: no parameter passed will delete node at end of list"""
        #  check if list is empty 
        if not self.head:
            return print('DLL is empty')
        else:
            # if not, and index for deletion is 0
            if index == 0:
                # set node to pointer location/head
                node = self.head
                # set head pointer to node after first node 
                self.head = self.head.next
                # set prev pointer of node past node being deleted to None 
                node.prev = None
            # if no index value passed into method, delete node at end of list
            elif index == 'end':
                # check if only node
                if self.head == self.tail:
                    # if so, delete node and therefore list
                    self.head = None
                    self.tail = None 
                else:
                    # check to see if this is only node in list
                    # then delete only node 
                    if self.tail == self.head:
                        self.head = None
                        self.tail = None 
                    else:
                        # if not only node in list reassign tail 
                        self.tail = self.tail.prev
                        self.tail.next = None 
            else:
                # anywhere else in list 
                # set current node
                if self.head == self.tail and index >= 1:
                    return print('Index out of range')
                node = self.head
                if not node.next.next and index != 1:
                    return print('Index out of range')
                elif not node.next.next and index == 1:
                    self.tail = node
                    node.next = None
                    return
                counter = 0
                while counter < index-1:
                    node = node.next 
                    # check if index out of range
                    if node.next.next == None and index-counter>2:
                        return print('Index out of range')
                    # check to see if final node
                    elif node.next.next == None and node.next.prev == node:
                        # if it is set tail to node and node.next to None, and return 
                        self.tail = node
                        node.next = None
                        return
                    else:
                        counter += 1 
                # else, not final node
                node.next = node.next.next
                node.next.prev = node

                        
    def deleteAllDLL(self):
        """method to delete all of DLL"""
        # if DLL is empty print 
        if not self.head:
            return print('DLL is empty')
        else:
            # traverse through list and set all prev pointers of each node to None, therefore deleting link 
            node = self.head
            while node.next:
                node.prev = None
                node = node.next
            # then set tail and head to none, deleting list 
            self.head = None 
            self.tail = None   
            return print('DLL has been deleted')


    def printDLL(self):
        """method to print DLL"""
        # if DLL is empty print 
        if not self.head:
            return print("DLL is empty")
        else:
            result = []
            node = self.head
            while node:
                result.append(node.data)
                node = node.next
            return print(result)

    def reversePrintDLL(self):
        """method to reverse print DLL"""
        if not self.head:
            return print("DLL is empty")
        else:
            result = []
            node = self.tail
            while node:
                result.append(node.data)
                node = node.prev
            return print(result)

if __name__ == "__main__":
    print('start')
    # create DLL from DLL class
    DLL = DoubleLinkedList()
    # create the DLL with function nd itialise with value 
    DLL.createDLL(5)
    # print DLL
    DLL.printDLL()
    # DLL.insertDLL(2,0)
    DLL.insertDLL(3,0)
    DLL.insertDLL(4,0)
    DLL.insertDLL(55,0)
    DLL.insertDLL(6,3)
    DLL.insertDLL(17)
    DLL.printDLL()
    DLL.reversePrintDLL()
    DLL.searchValueDLL(1)
    DLL.printDLL()
    DLL.deleteNodeOfDLL(0)
    DLL.printDLL()
    DLL.deleteNodeOfDLL(5)
    DLL.printDLL()
    DLL.deleteNodeOfDLL(5)
    DLL.printDLL()
    DLL.deleteNodeOfDLL(5)
    DLL.reversePrintDLL()
    DLL.printDLL()
    DLL.deleteNodeOfDLL(2)
    DLL.deleteNodeOfDLL()
    DLL.reversePrintDLL()
    DLL.deleteNodeOfDLL()
    DLL.reversePrintDLL()
    DLL.deleteNodeOfDLL(5)
    DLL.printDLL()
    DLL.deleteNodeOfDLL(1)
    DLL.reversePrintDLL()
    DLL.printDLL()
    DLL.deleteAllDLL()


    print('complete')



