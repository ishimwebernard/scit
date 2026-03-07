class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            print("The list is empty")
        
        temp = self.head
        strresult = ''
        while temp:
            strresult += str(temp.data)
            temp = temp.next
        print(strresult)

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
    
if __name__ == "__main__":
    list = List()
    list.insert_end(0)
    list.insert_begining(1)
    list.insert_begining(2)
    list.insert_begining(3)
    list.insert_end(0)
    list.insert_begining(0)
    list.print()
