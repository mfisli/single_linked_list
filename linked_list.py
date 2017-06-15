#linked_list.py
# This program demos the data structure of a single linked ist
from random import randint

class Node:
    # Node constructor to init node 
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node
        print("Node created with data: ", data)

class LinkedList():
    # Linked List constructor to init head 
    def __init__(self, head = None):
        self.head = head
        print("Linked list created.")
    # Insert new node in sorted order 
    def insert_sorted(self, new_node):
        # Am I the first one here? 
        if self.head is None:
            new_node.next = None
            self.head = new_node
        # Am I smaller than the head? 
        elif new_node.data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
        # Who is bigger than me? I need to be behind him. 
        else:             
            current_node = self.head #no need for last_node
            while (current_node.next is not None) and (current_node.next.data < new_node.data):
                current_node = current_node.next             
            new_node.next = current_node.next
            current_node.next = new_node
        print_nodes(self.head)
        print()
# Recursive method to print out the nodes 
def print_nodes(node):
    if node.data is not None:
        print("(", node.data, ")", sep="", end="")
    if node.next is not None:
        print(" -", node.next.data, "-> ", sep="", end="")
        print_nodes(node.next)



###############################################################################
# Main 
###############################################################################
'''
(1) -> (2) -> (3)
'''
ll = LinkedList()
ll.insert_sorted(Node(6))
ll.insert_sorted(Node(2))
ll.insert_sorted(Node(4))
ll.insert_sorted(Node(3))
ll.insert_sorted(Node(5))
ll.insert_sorted(Node(1))








