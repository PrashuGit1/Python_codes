class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def add_node(head, new_node, position):

    if position==1:
        new_node.next=head
        return head
    
    current_node=head
    for i in range(position-2):
        current_node=current_node.next
    new_node.next=current_node.next
    current_node.next=new_node
    
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)
node6=Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = add_node(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)