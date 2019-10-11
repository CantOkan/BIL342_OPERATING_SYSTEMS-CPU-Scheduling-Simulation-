import random
import queue

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
    
    def get(self,Process):
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


    def PopProcess(self):
        cur_node=self.head

        while cur_node.next !=None:
            prev=cur_node
            cur_node=cur_node.next
        
       # print(cur_node.data)
        prev.next=None  
        return cur_node.Process


class FCFS(object):
    adet=0
    def __init__(self):
        self.q=queue.Queue()

    def count(self):
        self.adet+=1

#get averaing lentgth
    def get(self,Process):
        if(Process!=None):
            self.q.put(Process)
            self.count()

    def show(self):
        print(self.q.qsize())

    def SendProcess(self):
        return self.q.get()





TotalProb=1
Queue1prob=0.5
Queue2prob=TotalProb-Queue1prob

class ReadyQueue(object):
    
    def __init__(self,len):
        self.lentgh=len
        self.Readyqueue=queue.Queue(maxsize=self.lentgh)
    

    def getProcess(self,Process):
        self.Readyqueue.put(Process)
        
    def passProcess(self):
        while (self.Readyqueue.qsize()>0):#Ready Q. proceess kalmayana kadar processleri FCFS 
            x=random.uniform(0,1)#SJF dağıt
            pro=self.Readyqueue.get()
            if(Queue1prob>x):
                print("Q1 gidiyor")
                Q1.get(pro)
            elif(x>=Queue2prob):
                print("Q2 gidiyor")
                Q2.get(pro)
        






ReadyQ=ReadyQueue(64)

Q1=FCFS()
Q2=SJF()


p1=Process(5,4,"id1")
p2=Process(5,4,"id2")
p3=Process(5,4,"id3")

ReadyQ.getProcess(p1)
ReadyQ.getProcess(p2)
ReadyQ.getProcess(p3)
ReadyQ.passProcess()
print("first time")
Q1.show()

Q2.display()


p4=Process(5,4,"id4")
p5=Process(5,4,"id5")
p6=Process(5,4,"id6")


ReadyQ.getProcess(p4)
ReadyQ.getProcess(p5)
ReadyQ.getProcess(p6)
ReadyQ.passProcess()

print("second time")
Q1.show()

Q2.display()

