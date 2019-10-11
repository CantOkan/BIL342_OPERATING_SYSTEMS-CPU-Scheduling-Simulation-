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
        if cur.data != None:
            while cur.next!=None:
                cur=cur.next
            cur.next=new_node
        else:
            self.head=new_node
            
        

    def length(self):
        cur=self.head
        total=0

        while cur.next!=None:
            cur=cur.next
            total+=1
        return total
    

    def display(self):
        elems=[]

        cur_node=self.head

        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
            
            
            
        print(elems)

    def get(self,index):
        if index>=self.length:
            print("Error 'get' Index out of range")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next

            if cur_idx==index:
                return cur_node.data
            cur_idx+=1

    def erase(self,index):
        if index>=self.length():
            print("Error 'erase' Index out of range")
            return
        cur_idx=0
        cur_node=self.head

        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1

mylist=LinkedList()

mylist.append(1)
mylist.append(5)

mylist.display()
                

        
