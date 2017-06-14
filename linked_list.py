#linked_list.py
# This program demos the data structure of a single linked ist

class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        print("Node created with data",data)

# My module
class Head(object):
    def __init__(self, node):
        self.current_head = node
        print("Head created with data", node.data)
    def set_head(self,node):
        self.current_head = node
        print("New head is", node.data)

def print_nodes(node):
    print("(", node.data, ")", sep="",end="")
    if node.next_node is not None:
        print(" -> ",end="")
        print_nodes(node.next_node)
    else:
        print("\n")

def considering(node1,node2):
    print(node1.data,"vs",node2.data)

def add_node(head,data):
    new_node = Node(data)
    current_node = None
    last_node = None
    # if bigger put in front
    considering(new_node,head.current_head)
    if new_node.data < head.current_head.data:
        new_node.next_node = head.current_head
        head.set_head(new_node)
        return
    current_node = head.current_head.next_node

    while new_node.data > current_node.data: 
        considering(new_node,current_node)
        last_node = current_node 
        current_node = current_node.next_node
        print("current node: (", current_node.data, ")", sep="")
        print("last node: (", last_node.data,")", sep="")

    new_node.next_node = current_node
    last_node.next_node = new_node




###############################################################################
# Main 
###############################################################################
'''
(1) -> (2) -> (3)
'''
node3 = Node(4)
node2 = Node(2, node3)
node1 = Node(1, node2)
head = Head(node1)

print_nodes(head.current_head)
add_node(head,3)
print_nodes(head.current_head)


