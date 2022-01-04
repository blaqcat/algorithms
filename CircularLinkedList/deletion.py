
from markupsafe import re


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if  node == self.tail.next:
                break

     # Creation of circular singly linked list
    def create_c_sll(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    # Insertion of a node in circular singly linked List

    def insert_c_sll(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            return "The node has been successfully created"



    # Search for a node in circular singly linked list
    def search_c_sll(self, node_value):
        if self.head == None:
            return "There is no node in this CircularSinglyLinkedList"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return "The node does not exist in this CircularSinglyLinkedList"
    
    # Delete a node from circular singly linked List
    def delete_node_c_sll(self, location):
        if self.head is None:
            print("There is not any node in CSL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next =None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next =None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head.next
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
    
    # Delete entire circular singly linked list
    def delete_entire_c_sll(self):
        self.head = None
        self.tail.next = None












circular_sll = CircularSinglyLinkedList()
circular_sll.create_c_sll(1)
circular_sll.insert_c_sll(0, 0)
circular_sll.insert_c_sll(2,1)
circular_sll.insert_c_sll(2,1)
circular_sll.insert_c_sll(3,1)
circular_sll.insert_c_sll(2,2)
print([node.value for node in circular_sll])


circular_sll.delete_node_c_sll(2)
print([node.value for node in circular_sll])

circular_sll.delete_entire_c_sll()
print([node.value for node in circular_sll])