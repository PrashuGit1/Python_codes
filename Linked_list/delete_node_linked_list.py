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


def delete_node(head, node_to_delete):

    if head == node_to_delete:
        return head.next
    current_node=head

    while current_node:
        if current_node.next==node_to_delete:
            current_node.next=node_to_delete.next
            break
        current_node=current_node.next
    
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = delete_node(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)