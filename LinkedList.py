class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

ll = LinkedList()
while True:
    print("\n1.Insert 2.Delete 3.Display 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1: ll.insert_end(input("Enter data: "))
    elif ch == 2: ll.delete(input("Enter value to delete: "))
    elif ch == 3: ll.display()
    elif ch == 4: break
