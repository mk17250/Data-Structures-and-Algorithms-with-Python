
class createNode:
    """Node class"""
    def __init__(self, data=None):
            self.data = data
            self.next = None 


class CSLL:
    """CSLL class"""
    def __init__(self):
        self.head = None

    def createCSLL(self, data=None):
        """method to create CSLL"""
        newNode = createNode(data)
        self.head = newNode
        newNode.next = self.head


    def insertIntoCSLL(self, data, index='end'):
        """Note - if index parameter not passed will insert at the end of CSLL """
        """Note - the first call of this funnction will position the node after the first node created when initalising the instance, unless 0 is passed"""
        newNode = createNode(data)
        node = self.head
        # if CSLL only has one node, insert after node 1 
        if node.next == node:
            if index == 0:
                self.head.next = newNode
                newNode.next = self.head
                self.head = newNode
            else:
            # print('ok')
                node.next = newNode
                newNode.next = self.head
        # if no parameter for index passed insert at end of CSLL
        else:
            if index == 'end':
                # print('yes')
                while True:
                    node = node.next
                    if node.next == self.head:
                        node.next = newNode
                        newNode.next = self.head
                        break
            # insert at start of CLL
            elif index == 0:
                newNode.next = self.head
                self.head = newNode
                while True:
                    node = node.next
                    if node.next == self.head.next:
                        node.next = self.head
                        break
            # insert anywhere else remaining CSLL
            else:
                # print('me')
                counter = 0 
                while counter < index-1:
                    node = node.next
                    if node == self.head:
                        print('Index out of range')
                        return None
                    else:
                        counter += 1 
                newNode.next = node.next
                node.next = newNode

    def printCSLL(self):
        """print CSLL"""
        result=[]
        if not self.head:
            return print("CSLL is empty") 
        node = self.head
        result.append(node.data)
        if node.next == self.head:
            return print(result)
        else:
            while True:
                # print('here1')
                node = node.next
                result.append(node.data)
                if node.next == self.head:
                    break
        return print(result)

    def searchValue(self, value):
        """search for value in list and return value if found else 'Value not in CSLL' message"""
        node = self.head
        if node.data == value:
            return print(node.data)
        else:
            while True:
                node = node.next
                if node.data == value:
                    return print(node.data)
                else:
                    if node.next == self.head:
                        return print('Value not in CSLL')

    def searchValueIndex(self, index_val=0):
        """search the CSLL and return data at given index, return out range if not in range od CSLL"""
        node = self.head
        if index_val == 0:
            return print(self.head.data)
        elif index_val == 1:
            if self.head.next == self.head:
                return print('Index out of range')
            else:
                return print(node.next.data)
        else:
            index_counter = 1
            node=node.next
            while index_counter < index_val:
                if node.next == self.head:
                    return print('Index value out of range of CSLL')
                else:
                    node = node.next
                    index_counter+=1
            return print(node.data)

    def deletionFromCSLL(self, deletion_index = 'end'):
        """delete node from CSLL at begining, end or middle - NOTE: pass no deletion_index value to delete from end of CSLL"""
        if self.head.next == self.head:
                self.head = None
                return print("Only one node in CSLL, CSLL has been deleted")
        #  delete first node 
        elif deletion_index == 0:
            if self.head.next == self.head:
                self.head = None
                return print("Only node in CSLL, CSLL has been deleted")
            else: 
                node = self.head
                while True:
                    node = node.next
                    if node.next == self.head:
                        break
                self.head = self.head.next
                node.next = self.head
        # delete last node 
        elif deletion_index == 'end':
            node = self.head
            while True:
                node = node.next
                if node.next.next == self.head:
                    node.next = self.head
                    break
        # delete from anywhere else in CSLL
        else:
            index_count = 0
            node = self.head
            while index_count < deletion_index-1:
                if node.next.next == self.head:
                    return print("deletion index out of range")
                else:
                    node = node.next
                    index_count += 1
            node.next = node.next.next

    def deleteAllCSLL(self):
        """method to delete all of CSLL"""
        if self.head.next == self.head:
                self.head = None
        else:
            node = self.head
            while True:
                node = node.next
                if node.next == self.head:
                    node.next = None
                    break
            self.head = None 
            

print('start')

if __name__ == '__main__':

    newCSLL = CSLL()
    newCSLL.createCSLL(55)
    newCSLL.insertIntoCSLL(2)
    newCSLL.insertIntoCSLL(3)
    newCSLL.insertIntoCSLL(4)
    newCSLL.insertIntoCSLL(5)
    newCSLL.insertIntoCSLL(6,5)
    newCSLL.printCSLL()
    newCSLL.searchValueIndex(3)
    newCSLL.searchValueIndex()
    newCSLL.searchValue(5)
    newCSLL.printCSLL()
    newCSLL.deletionFromCSLL(4)
    newCSLL.printCSLL()
    newCSLL.deleteAllCSLL()
    newCSLL.printCSLL()

    print('complete')

    