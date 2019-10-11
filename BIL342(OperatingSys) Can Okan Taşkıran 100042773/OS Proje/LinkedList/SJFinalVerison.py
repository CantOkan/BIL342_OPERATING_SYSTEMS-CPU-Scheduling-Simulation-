
class Process(object):
    waiting_time=0
    def __init__(self,burst_size,Arr_time,id):
        self.id=id
        self.burst_size=burst_size
        self.Arr_time=Arr_time
    def getwaitingtime(self):
        return self.waiting_time 


class node(object):
    def __init__(self,Process=None):
        self.Process=Process
        self.next=None


class SJF(object):
    def __init__(self):
        self.head=node()
    
    def append(self,Process):
        new_node=node(Process)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            if(cur.Process.burst_size<Process.burst_size):
                sakla=cur.Process
                cur.Process=new_node.Process
                new_node.Process=sakla
    
        
        cur.next=new_node


    def display(self):
        elems=[]

        cur_node=self.head

        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.Process.id)
        print(elems)


    def pop(self):
        cur_node=self.head

        while cur_node.next !=None:
            prev=cur_node
            cur_node=cur_node.next
        
       # print(cur_node.data)
        prev.next=None  
        return cur_node.Process


#Burst size göre
#P2-P1-P3 olmalı
p1=Process(3,0,'id1')
p2=Process(5,1,'id2')
p3=Process(1,1,'id3')

SJF1=SJF()


SJF1.append(p1)
SJF1.append(p2)

SJF1.display()

print('Process geldikten sonra')

SJF1.append(p3)

SJF1.display()


print("Poped Process :"+str(SJF1.pop().id))

print("After delletee")

SJF1.display()