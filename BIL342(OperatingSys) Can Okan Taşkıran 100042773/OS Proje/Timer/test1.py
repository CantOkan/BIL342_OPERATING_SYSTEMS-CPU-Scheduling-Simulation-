import random
import queue
from threading import Timer

class Process(object):
    waiting_time=0
    def __init__(self,burst_size,Arr_time,id):
        self.id=id
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


def sendQueue(Process):
    if(True):
        fcfs.get(Process)
        

def createProcess(i):
        burstSize=5
        Arr_time=i
        idim="id"+str(i)
        process=Process(burstSize,Arr_time,idim)
        Timer(Arr_time,sendQueue,[process]).start()
        return process


fcfs=FCFS()


createProcess(1)
createProcess(2)
print(createProcess(3).id)

print(createProcess(5).id)

while True:
    fcfs.show()


