# Created by Black Cat
# Copyright 2021

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





singly_linked_list = SLinkedList()
singly_linked_list.insert_sll(1,1)
singly_linked_list.insert_sll(2, 1)
singly_linked_list.insert_sll(3, 1)
singly_linked_list.insert_sll(4, 1)
print([node.value for node in singly_linked_list])