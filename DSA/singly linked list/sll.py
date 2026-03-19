# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    # Insert at end
    def insert_end(self, value):
        newnode = Node(value)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode

    # Insert in between (after key)
    def insert_between(self, key, value):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Key not found!")
            return

        newnode = Node(value)
        newnode.next = temp.next
        temp.next = newnode

    # Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        prev = None

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None

    # Delete in between (by key)
    def delete_between(self, key):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Node not found")
            return

        prev.next = temp.next

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main menu
def main():
    ll = SinglyLinkedList()

    while True:
        print("\n1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert in Between")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete in Between")
        print("7. Display List")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            ll.insert_beginning(value)

        elif choice == 2:
            value = int(input("Enter value: "))
            ll.insert_end(value)

        elif choice == 3:
            key = int(input("Enter key value: "))
            value = int(input("Enter new value: "))
            ll.insert_between(key, value)

        elif choice == 4:
            ll.delete_beginning()

        elif choice == 5:
            ll.delete_end()

        elif choice == 6:
            key = int(input("Enter value to delete: "))
            ll.delete_between(key)

        elif choice == 7:
            ll.display()

        elif choice == 8:
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()