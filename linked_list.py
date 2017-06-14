#linked_list.py
# This program demos the data structure of a single linked ist

class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        print("Node created with data: ", data)

class Head(object):
    def __init__(self, head = None):
        self.current_head = head
        print("Head created.")

def print_nodes(node):
    # check if head
    if node.data is not None:
        print("(", node.data, ")", sep="", end="")
    if node.next_node is not None:
        print(" -", node.next_node.data, "-> ", end="")
        print_nodes(node.next_node)
    print("\n")

def considering(node1,node2):
    print(node1.data,"vs",node2.data)

def insert(data):
    #make a new node
    new_node = Node(data)
    # if there is no head, then make new node the head
    if head.current_head is None:
        head.current_head = new_node
        print("\t New node", new_node.data, "is the first.")
    # if you are smaller than the head, then make the new node the head
    elif new_node.data < head.current_head.data:
        print("current head is: ", head.current_head.data)
        new_node.next_node = head.current_head
        print("new_node.next_node:", new_node.next_node.data)
        head.current_head = new_node
        print("\t New node", new_node.data, "is the the new head.")
        print_nodes(head.current_head)
        return
    # if you are the biggest, then make the new node the last one
    current_node = head.current_head
    while current_node.data is not None or new_node.data > current_node.data:
        considering(new_node,current_node)
        current_node = current_node.next_node
    current_node.next_node = new_node
    print_nodes(head.current_head)


    

###############################################################################
# Main 
###############################################################################
'''
(1) -> (2) -> (3)
'''
head = Head()
insert(3)
insert(2)
insert(1)




