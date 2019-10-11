class node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList(object):
    def __init__(self):
        self.head=node()
    
    def append(self,data):
        new_node=node(data)
        cur=self.head
        
        while cur.next!=None:
            cur=cur.next
            if(cur.data>data):
                sakla=cur.data
                cur.data=new_node.data
                new_node.data=sakla
                    
        
        cur.next=new_node
    
    def display(self):
        elems=[]

        cur_node=self.head

        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
        

    def pop(self):
        cur_node=self.head

        while cur_node.next !=None:
            prev=cur_node
            cur_node=cur_node.next
        
       # print(cur_node.data)
        prev.next=None   






list=LinkedList()

list.append(5)
list.append(6)

list.append(3)

list.display()


print("-------------")

list.append(2)

list.append(7)
list.append(1)

list.display()

list.pop()

print("----------del-----")
list.display()