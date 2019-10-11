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



Cpu=CPU(1)
Queue1=FCFS()
Queue2=SJF()

process1=Process(5,1,"id1")
process2=Process(8,0,"id2")
Queue2.get(process1)
Queue2.get(process2)

Queue2.display()



Cpu.checkCpu()

Cpu.checkCpu()


