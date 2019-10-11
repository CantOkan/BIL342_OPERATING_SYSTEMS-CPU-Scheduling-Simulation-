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
    def __init__(self,core,liste):
        self.core=core
        self.liste=liste

    def checkCpu(self):
        if(liste==0):
            getProcess(Queue1.SendProcess())


    def getProcess(self,Process):
        for i in (0,len(Process.burst_size)):
            Process.burst_size-=1





p1=Process(5,0)
p2=Process(5,1)

Queue1=FCFS()

Queue1.get(p1)
Queue1.get(p2)

Queue1.show()

print(Queue1.SendProcess().Arr_time)
print(Queue1.SendProcess().Arr_time)
