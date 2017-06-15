#linked_list.py
import random
#//////////////////////////////////////////////////////////////////////////////
# Represents a node with data and a link to the next node 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        print("Created Node", self.data)
#//////////////////////////////////////////////////////////////////////////////
# Linked List Class that keeps nodes connected to one another with a single link  
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        print("Linked List is up.")
    #__________________________________________________________________________
    # Inserts a new node in sorted order when given data
    def insert(self,data):
        new_node = Node(data)
        # Am I the first one here?
        if self.head is None:
            self.head = new_node
            print("\tNew node", data,"is first one here.")
        # Am I smaller than the head?
        elif new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            print("\tNew node", data,"is new head.")
        # Who is bigger than me?
        else:
            current = self.head
            while current.next is not None and new_node.data > current.next.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            print("\tInserted", new_node.data, "after", current.data)
        self.print_nodes(self.head)
    #__________________________________________________________________________
    # Attmpts to find a target node and deletes it
    # This method could be decomposed - it's a bit long
    def delete_node(self,target):
        print("\nStarting search for target: [", target,"]")
        found = False
        result = "Delete Failed"
        # Is there a head?
        if self.head is None:
            result = "No head found."
        # Is the head the first target?
        elif self.head.data == target:
            result = "Target " + str(self.head.data) + " is the head." 
            self.head = self.head.next
        # Is the target found or are there targets left?
        else:
            count = 0
            current = self.head
            last = None
            while not found and current is not None:
                count += 1
                if current.data == target:
                    found = True
                else:
                    last = current
                    current = current.next
            if found:
                result = ("Target " + str(current.data) + 
                    " deleted after " + str(count) + " attemp(s).")
                last.next = current.next
                current.next = None

            else:
                result = ("Target not found after " + 
                    str(count) + " attemp(s).")
        self.print_nodes(self.head)
        return result
    #__________________________________________________________________________
    # Recursive method to print all nodes  
    def print_nodes(self,node):
        if node is not None:
            print("[",node.data,"]",end='')
        if node.next is not None:
            print("->",end='')
            self.print_nodes(node.next)
        else:
            print('')
###############################################################################
# Main
ll = LinkedList()
# Make a list of random data numbers 
my_list = random.sample(range(1, 101), 10)
# Insert test
for i in my_list:
    ll.insert(i)
# Delete node test 
target = random.choice(my_list)
print("\t",ll.delete_node(target))








