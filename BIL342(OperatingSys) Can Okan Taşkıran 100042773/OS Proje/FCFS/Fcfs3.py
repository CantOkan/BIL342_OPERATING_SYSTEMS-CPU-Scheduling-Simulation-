import random
import queue


class Process(object):
    waiting_time=0
    def __init__(self,burst_size,Arr_time):
        self.burst_size=burst_size
        self.Arr_time=Arr_time
    def getwaitingtime(self):
        return self.waiting_time 

    
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
            process=Queue1.SendProcess()
            self.unit.append(process)
            self.work(process)
        
            
    
    def work(self,Process):
        i=Process.burst_size
        while i!=0:
            print(i)
            i-=1
        x=self.unit.pop()
        print("Arrive time :"+str(x.Arr_time))

cpu=CPU(1)


p1=Process(5,0)
p2=Process(3,1)

Queue1=FCFS()

Queue1.get(p1)
Queue1.get(p2)




cpu.checkCpu()
cpu.checkCpu()

