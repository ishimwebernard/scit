class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty LinkedList")

        temp = self.head
        liststring = ''
        while temp:
            liststring = liststring + str(temp.data)
            temp = temp.next
            
        print(liststring)
if __name__ == "__main__":
    doubleLinkedList = DoubleLinkedList()
    doubleLinkedList.insert(1)
    doubleLinkedList.insert(2)
    doubleLinkedList.print()