# Created by Jerru Ngakana Monyelo
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



    
                




circular_dll =  CircularDoublyLinkedList()
circular_dll.create_dll(5)
print([node.value for node in circular_dll])
circular_dll.insertion_cdll(0,0)
circular_dll.insertion_cdll(1,1)
print([node.value for node in circular_dll])
circular_dll.traverse_cdll()