class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
        
    def print(self):
        if self.head is None:
            print("Empty Queue")
        
        printtemp = self.head
        stringout = ''
        while printtemp:
            stringout += str(printtemp.data) + ","
            printtemp = printtemp.next
            

        print(stringout)

    def delete(self):
        if self.head is None:
            print("The queue is already empty")

        self.head = self.head.next
        if self.head is None:
            self.tail = None


if __name__ == "__main__":
    queue = Queue()
    queue.insert(2)
    queue.print()
    queue.insert(3)
    queue.print()
    queue.delete()
    queue.print()
        
