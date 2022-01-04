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


    #  Traversable Method in Doubly Linked DoublyLinkedList
    def traversal_dll(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    # Reverse Traversal method in Doubly Linked List
    def reverse_traversal_dll(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev

    
    # Delete a node from a Doubly Linked List

    def delete_node(self, location):
        if self.head is None:
            print("There is no element in the in the DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                curr_node.next = curr_node.next.next
                curr_node.next.prev = curr_node
            print("The node has been succesfully deleted")


    # Delete entire Doubly Linked List
    def delete_dll(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")




                

            

        




doubly_linked_list = DoublyLinkedList()
doubly_linked_list.create_dll(5)
print([node.value for node in doubly_linked_list])
doubly_linked_list.insert_dll(0, 0)
doubly_linked_list.insert_dll(11, 0)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete_node(0)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete_dll()
print([node.value for node in doubly_linked_list])
     