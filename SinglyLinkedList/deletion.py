class Node:
    def __init__(self, value=None):
        self.value =value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insertion method
    def insert_sll(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node
                temp_node.next = new_node
                new_node.next = next_node
    # Traverse node in a Singly linked list
    def traverse_sll(self):
        if self.head is None:
            print('The Singly Linked List does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Delete a node from Singly Linked List
    def delete_node(self, location):
        if self.head is None:
            print("The SLL does not exit")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
    
    #Delete Entire Singly_Linked
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

singly_linked_list = SLinkedList()
singly_linked_list.insert_sll(1, 0)
singly_linked_list.insert_sll(2, 1)
singly_linked_list.insert_sll(3, 1)
singly_linked_list.insert_sll(4, 1)

print([node.value for node in singly_linked_list])
singly_linked_list.delete_node(1)
print([node.value for node in singly_linked_list])

