import random
import queue
from threading import Timer
import time

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
        return len(elems)


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
        print("FCFS size:{}".format(self.q.qsize()))

    def SendProcess(self):
        return self.q.get()



class CPU(object):
    unit=list()

    def __init__(self,core):
        self.core=core
       

    def checkCpu(self):
        if(len(self.unit)==0):
            Process=Queue2.PopProcess()
            self.unit.append(Process)
            self.work(Process)
        
            
    
    def work(self,Process):
        i=Process.burst_size
        while i!=0:
            print(i)
            i-=1
        x=self.unit.pop()
        print("ID: :"+str(x.id))



TotalProb=1
Queue1prob=0.5
Queue2prob=TotalProb-Queue1prob

def sendQueue(Process):
    x=random.uniform(0,1)
    if(Queue1prob>x):
        print("Process "+str(Process.id)+" FCFS gidiyor")
        Queue1.get(Process)
    elif(x>=Queue2prob):
        print("Process "+str(Process.id)+" SJF gidiyor")
        Queue2.get(Process)
        

def createProcess(i):
        burstSize=5
        Arr_time=i
        idim="id"+str(i)
        process=Process(burstSize,Arr_time,idim)
        Timer(Arr_time,sendQueue,[process]).start()
        return process




Cpu=CPU(1)
Queue1=FCFS()
Queue2=SJF()



createProcess(1)
createProcess(2)
createProcess(3)
print("process"+str(createProcess(4)))
print("process"+str(createProcess(5)))


while True:#display Queues size
    time.sleep(1)
    Queue1.show()
    print("SJF size:{}".format(Queue2.display()))

