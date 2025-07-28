
class node:
    def __init__(self, data):
        self.data=data
        self.next=None

node1=node(3)
node2=node(5)
node3=node(4)
node4=node(8)
node5=node(9)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

current_node=node1

while current_node:
    print(current_node.data, end='->')
    current_node=current_node.next
print("Null")