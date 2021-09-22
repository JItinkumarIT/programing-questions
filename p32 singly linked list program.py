class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
#node1=Node(10)
#print(node1)

class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
            if n is None:
                print("Node is not predent in Linked List")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node


    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
            if n.ref is None:
                print("Node is not found!")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
                

LL1=LinkedList()
LL1.add_before(30,10)
#LL1.add_end(30)
#LL1.add_begin(20)
LL1.add_begin(10)
#LL1.add_after(30,20)
LL1.print_LL()
