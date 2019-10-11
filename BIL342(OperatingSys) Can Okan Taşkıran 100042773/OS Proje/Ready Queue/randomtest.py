import random
import queue
x=random.uniform(0,1)

print(x)

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



fc=FCFS()
Pr1=Process(5,1,"id1")
Pr2=Process(5,1,"id1")
Pr3=Process(5,1,"id1")
Pr4=Process(5,1,"id1")
Pr5=Process(5,1,"id1")

#liste=[]

#liste.append(Pr1,Pr2,Pr3)

fc.get(Pr1)
fc.get(Pr2)
fc.get(Pr3)
fc.get(Pr4)

print(fc.SendProcess().id)
fc.show()

fc.get(Pr5)

fc.show()


