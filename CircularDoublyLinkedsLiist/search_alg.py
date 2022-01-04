# Created by Jerry Ngakana Monyelo
# All Copyrights to the algorithm reserved


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    # Creation of a Circular Doubly Linked List

    def create_dll(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        print( "CDLL has been succefully created")

    # Insertion Method in Circular Doubly-linked List
    def insertion_cdll(self, value, location):
        if self.head is None:
            return "The CDLL does not  exist"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            print(" The node has been succesfully inserted into the CDLL")

    # Traversal of Circular Doubly Linked List
    def traverse_cdll(self):
        if self.head is None:
            print("There is no node to do any traversal")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next


    # Search Circular Doubly Linked List
    def search_cdll(self, node_value):
        if self.head is None:
            print("There is no node to traverse")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    print(temp_node.value)
                if temp_node == self.tail:
                    return "The vlaue does not exist in this CDLL"
                temp_node = temp_node.next

    # Delete a node from Circular Doubly Linked List
    def delete_node(self, location):
        if self.head is None:
            print("There is no node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                curr_node.next = curr_node.next.next
                curr_node.next.prev = curr_node
            print("The node has been succesfully deleted")



    # Delete entire Circular Doubly Linked List
    def delete_cdll(self):
        if self.head is None:
            print("There is no Circular Doubly Linked List to delete")
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The Circular Doubly Linked List has been successfully deleted")




circular_dll =  CircularDoublyLinkedList()
circular_dll.create_dll(5)
print([node.value for node in circular_dll])
circular_dll.insertion_cdll(0,0)
circular_dll.insertion_cdll(1,1)
print([node.value for node in circular_dll])
circular_dll.traverse_cdll()
circular_dll.search_cdll((6))
circular_dll.delete_node(0)
print([node.value for node in circular_dll])
circular_dll.delete_cdll()
print([node.value for node in circular_dll])