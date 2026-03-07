class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

    
class Stack:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def remove(self):
        if self.head is None:
            print("Stack already empty")
            return
        
        temp = self.head
        self.head = temp.next

    def print(self):
        if self.head is None:
            print("Stack is empty")
            return

        temp = self.head
        stackstr = ''

        while temp:
            stackstr = stackstr + str(temp.data) + "\n __"
            temp = temp.next

        print(stackstr)



if __name__ == "__main__":
    stack = Stack()
    stack.insert(1)
    stack.insert(2)
    stack.insert(3)
    stack.insert(4)
    stack.insert(5)
    stack.insert(6)
    stack.insert(7)
    stack.remove()
    stack.print()
