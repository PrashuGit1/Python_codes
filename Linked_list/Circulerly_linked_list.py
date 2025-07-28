class node:
    def __init__(self, data):
        self.data=data 
        self.next=None
        self.previous=None

node1=node(5)
node2=node(9)
node3=node(2)
node4=node(8)

node1.previous=node4
node1.next=node2

node2.previous=node1
node2.next=node3

node3.previous=node2
node3.next=node4

node4.previous=node3
node4.next=node1



print('\nTraversing Farword')
current_node=node1
start_node=node1
print(current_node.data, end='->')
current_node=current_node.next

while current_node!=start_node:
    print(current_node.data, end='->')
    current_node=current_node.next
print('...')



print('\nTraversing Backword')
current_node=node4
start_node=node4
print(current_node.data, end='<-')
current_node=current_node.previous

while(current_node!=start_node):
    print(current_node.data, end='<-')
    current_node=current_node.previous
print('...')