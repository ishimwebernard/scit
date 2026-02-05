class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")

        temp = self.head
        liststr = ''

        while temp:
            liststr += str(temp.data) + '-->'
            temp = temp.next

        print(liststr)
    
    def delete(self, value):
        if self.head is None:
            print("Deletion impossible")
        head_temp = self.head
        while head_temp:
            if head_temp.data == value:
                print("Deleted Item", str(head_temp.data))
                head_temp.next = head_temp.next.next
                break
            head_temp = head_temp.next
        
        

if __name__ == "__main__":
    linklist = LinkedList()
    linklist.insert_at_beginning(1)
    linklist.insert_at_beginning(34)
    linklist.print()

