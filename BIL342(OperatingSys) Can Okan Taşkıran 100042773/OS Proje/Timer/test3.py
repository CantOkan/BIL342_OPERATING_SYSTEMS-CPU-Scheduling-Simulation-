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


def show(Process):
    print(Process.id)
    

def createProcess(i):
        burstSize=5
        Arr_time=i
        idim="id"+str(i)
        process=Process(burstSize,Arr_time,idim)
        Timer(Arr_time,show,[process]).start()
        return process



print(createProcess(1).id)
print(createProcess(5).id)
