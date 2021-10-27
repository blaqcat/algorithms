class Node:
    def __init__(self, value):
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
            if node == self.tail.next:
                break


    # Creation of circular singly linked list
    def create_c_sll(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

circular_sll = CircularSinglyLinkedList()
circular_sll.create_c_sll(1)

print([node.value for node in circular_sll])