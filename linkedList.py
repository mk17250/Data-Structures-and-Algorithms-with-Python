
class Node:
    """Node class"""
    def __init__(self, data=None):
        # node attributes 
        self.data = data
        self.next = None


class SLinkedList:
    """Single Linked List class"""
    def __init__(self):
        #  linked list attributes 
        self.head = None
        # self.tail = None

    # create this code so list can be printed
    def printSSL(self):
        """method to print out SLL"""
        # check list is not empty 
        if self.head == None:
            print('list is empty')
            return None 
        result = []
        node = self.head
        result.append(node.data)
        while node.next != None:
            node = node.next
            result.append(node.data)
        print(result)


    # Search and print value at index given 
    def indexSLL(self, index_value):
        """method to return the value from a provided index"""
        # Check list is not empty
        if self.head == None:
            print('List is empty')
        else:
            node = self.head
            index = 0
            while index < index_value:
                node = node.next
                if node == None:
                    print('Index out of range')
                    return None 
                else:
                    index += 1    
            print(node.data)

    # Create a method to return the index of a given value
    def indexOfValue(self, data_value):
        """method which return the index of the value being searched for"""
        # start with head of SLL
        node = self.head
        # Set index counter to 0 
        index_val = 0
        # Check list is not empty
        # check list is not empty 
        if self.head == None:
            print('list is empty')
            return None 
        # if the vlaue in thr head of the SLL return 0
        elif node.data == data_value:
            return print(index_val)
        # else transverse through list and if node.next is None then return 'not in list', else if node.value == value return
        else:
            while True:
                node = node.next
                if node == None:
                    print('Not in list')
                    return None
                elif node.data == data_value:
                    return print(index_val+1)
                index_val += 1 
                 
    #  Create methd to insert into SLL
    def insertIntoSLL(self, data, index=None):
        """method to insert data value into chosen index of SLL"""
        """NOTE - pass in no index value to insert into end of SLL"""
        # Create new node with data value 
        newNode = Node(data)
        # check list is not empty 
        if self.head == None:
            print('list is empty')
            return None 
        # Inserting data into head of SLL 
        elif index == 0:
            # set pointer of new node to what was head 
            newNode.next = self.head
            # set head to newNode
            self.head = newNode
        # Insert data at end of SLL (tail)
        # set to head which points to first node
        elif index == None:
            node = self.head
            while node.next != None:
                prev_node = node
                node = node.next
            if node.next == None:
                node.next = newNode
        # Insert into anywhere else in the SLL
        else:
            node = self.head
            indexValue = 0
            while indexValue < index -1:
                node = node.next
                if node == None:
                    print('Insertion index out of range for SLL')
                    return None
                else:
                    indexValue += 1
            # it exits loop when it hits node prior to index value 
            # set pointer of new node to location of index node 
            newNode.next = node.next
            # change pointer of prior node to new node 
            node.next = newNode
    # Create method to delete node in list
    def deleteNode(self, index_value=0):
        """Method to delete node in linked list"""
        node = self.head
        counter = 0 
        if self.head == None:
            print('list is empty')
            return None 
        elif index_value == 0:
            self.head = self.head.next
        elif index_value == 1:
            node_after = node.next.next
            node.next = node_after
        else:
            while counter < index_value-1:
                node = node.next
                if node.next == None:
                    print('Index for deletion out of range of SLL')
                    return None
                else:
                    counter += 1
            node_after = node.next.next
            node.next = node_after

    def deleteSLL(self):
        """Deletes entire SLL"""
        self.head = None 
    
            
if __name__ == '__main__':
            
           
    # 1 First create a head and tail using SLinkedLList
    SinglyLinkedList = SLinkedList()
    # 2 Create two ndes with values 1 and 2 respectively 
    node1 = Node(11)
    node2 = Node(12)
    node3 = Node(13)
    node4 = Node(14)
    node5 = Node(15)
    # 3 Now need to link nodes togther. First assign node1 as head value
    SinglyLinkedList.head = node1
    # 4 Now link pointer of node1 to node2 
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # 5 Now assign the tail of the linked list to node2
    SinglyLinkedList.tail = node5 
    # 6 print list
    
    # Print list
    SinglyLinkedList.printSSL()
    # Index list
    SinglyLinkedList.indexOfValue(14)
    # Insert into list
    SinglyLinkedList.insertIntoSLL('Start', 0)
    # Inser into list
    SinglyLinkedList.insertIntoSLL('End')
    # Print statement 
    print('Prior to node deletion')
    # Print list
    SinglyLinkedList.printSSL()
    # Delete node from list 
    SinglyLinkedList.deleteNode(6)
    # Print statement
    print('Post node deletion')
    # Print list
    SinglyLinkedList.printSSL()
    print('before deleting entire list')
    SinglyLinkedList.deleteSLL()
    # Delete entire list 
    SinglyLinkedList.printSSL()
    # Print statement 
    print("complete")

    # ***** BRING ALL TOGETHER *****
    # Create new SLL, then use string formatting and globals function inside loop creating nodes with values 2-100 (evens), nodes called node1,....,node50
    empty_SSL = SLinkedList()
    num = 1
    mattsSLL = SLinkedList()
    for i in range(2,102,2):
        globals()[f"node{num}"] = Node(i)
        num+=1
    # Assign head to node 1 
    mattsSLL.head = node1

    # Attach pointers to next node using string formatting and global function in for loop 
    num1=2
    for j in range(1,50):
        globals()[f"node{j}"].next = globals()[f"node{num1}"]
        num1+=1
    # Call print function on new SLL
    mattsSLL.printSSL()
    # Delete SLL
    mattsSLL.deleteSLL()
   
    # **** NOTE - to improve this script it should be tested nd debugged (if required) more thoroughly ****