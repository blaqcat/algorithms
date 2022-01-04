# Created by Jerry Monyelo AWS Certified Solutions Architect - Associate


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    # Creation of Doubly Linked List
    def create_dll(self, node_value):
        node = Node(node_value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

        return "The DLL is created successfully"


    # Insertion Method in Doubly Linked List
    def insert_dll(self, node_value, location):
        if self.head is None:
            print("The Node cannot be inserted")
        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
            

        




doubly_linked_list = DoublyLinkedList()
doubly_linked_list.create_dll(5)
print([node.value for node in doubly_linked_list])
doubly_linked_list.insert_dll(0, 0)
doubly_linked_list.insert_dll(11, 0)
print([node.value for node in doubly_linked_list])
     