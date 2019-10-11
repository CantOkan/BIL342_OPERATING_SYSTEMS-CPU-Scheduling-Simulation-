#bu proje Queueların idle duruma geçtiğinde AWT ve ATTlerinin hesaplanması üzerine
#çalışıyorum

import random
import queue
from threading import Timer
import time

from multiprocessing import Process as pt

class Process(object):
    waiting_time=0
    TurnAround_time=0
    now=0
    end=0
    def __init__(self,burst_size,Arr_time,id,Queue=None):
        self.id=id
        self.burst_size=burst_size
        self.Arr_time=Arr_time
        self.startTurnAroundTime()#Process yaratıldığı anda sisteme girmiş durumda


    def SetQueue(self,Queueid):
        self.Queue=Queueid

    def GetQueue(self):
        return self.Queue

    def getwaitingtime(self):
        waiting_time=int(self.end-self.now)
        return waiting_time

    def startwaitingtime(self):
        self.now=time.time()

    def stopwaitingtime(self):
        self.end=time.time()


    def startTurnAroundTime(self):
        self.now=time.time()

    def stopTurnAroundTime(self):
        self.end=time.time()

    def getTurnAroundTime(self):
        TurnAround_time=int(self.end-self.now)
        return TurnAround_time

class node(object):
    def __init__(self,Process=None):
        self.Process=Process
        self.next=None


class SJF(object):
    totalTTA=0
    totalWaiting=0
    adet=0
    def __init__(self):
        self.head=node()


    def count(self):
        return self.adet
    
    def get(self,Process):
        self.adet+=1#for queue length
        
        Process.startwaitingtime()#for calcutating Waiting time

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
        return(len(elems))


    def PopProcess(self):
        cur_node=self.head
        
        while cur_node.next !=None:
            prev=cur_node
            cur_node=cur_node.next
        
       # print(cur_node.data)
        prev.next=None 

        cur_node.Process.stopwaitingtime()
        waiting_time=cur_node.Process.getwaitingtime()
        print("Waiting Time :"+str(waiting_time))
        self.addWaitingTime(waiting_time)

        return cur_node.Process


    def addWaitingTime(self,Waiting_Time):
        self.totalWaiting+=Waiting_Time

    def calculateWaitingTime(self):
        return self.totalWaiting/self.adet

    def setTurnAroundTime(self,zaman):
        print("TTA: "+str(zaman))
        self.totalTTA+=zaman

    def getAverageTurnAroundTime(self):
        return self.totalTTA/self.adet


class FCFS(object):
    totalTTA=0
    totalWaiting=0
    adet=0
    def __init__(self):
        self.q=queue.Queue()

    def count(self):
        return self.adet

#get averaing lentgth
    def get(self,Process):
        if(Process!=None):
            Process.startwaitingtime()
            self.q.put(Process)
            self.adet+=1

    def show(self):
        return self.q.qsize()

    def PopProcess(self):
        Process=self.q.get()
        Process.stopwaitingtime()
        waiting_time=Process.getwaitingtime()
        print("Waiting Time :"+str(waiting_time))
        self.addWaitingTime(waiting_time)
        return Process
        # return self.q.get()

    def addWaitingTime(self,Waiting_Time):
        self.totalWaiting+=Waiting_Time
       

    def calculateWaitingTime(self):
        return self.totalWaiting/self.adet
    

    def setTurnAroundTime(self,TTA_Time):
        self.totalTTA+=TTA_Time


    def getAverageTurnAroundTime(self):
        print("Total TTA:"+str(self.totalTTA))
        print("adet:"+str(self.adet))
        Average=self.totalTTA/self.adet
        print("Average TTA:"+str(Average))
       
    

class CPU(object):
    unit=list()

    TotalProb=1
    Queue1prob=0.5
    Queue2prob=TotalProb-Queue1prob

    def __init__(self,core):
        self.core=core
       

    def checkCpu(self):
        #x=random.uniform(0,1)
        x=0
        if(len(self.unit)==0 and Queue1.show()>0 and Queue2.display()>0):
            if(self.Queue1prob>x):
                print("fcfs pop")
                Process=Queue1.PopProcess()
                self.unit.append(Process)
                self.work(Process)

            elif(x>=self.Queue2prob):
                print("SJF pop")
                Process=Queue2.PopProcess()
                self.unit.append(Process)
                self.work(Process)

        elif(Queue1.show()>0):
            print("fcfs pop")
            Process=Queue1.PopProcess()
            self.unit.append(Process)
            self.work(Process)
        
        elif(Queue2.display()>0):
            Process=Queue2.PopProcess()
            self.unit.append(Process)
            self.work(Process)

        elif(Queue1.show()==0 and Queue2.display()==0):
            print("NOW you're in idle situation")
            print("FCFS adet: {}".format(Queue1.count()))
            print("SJF adet: {}".format(Queue2.count()))

            #Waiting_Time

            
            print("Total waitin time for FCFS : {}".format(Queue1.calculateWaitingTime()))

            ##Average Turn Around Time

            print("Average Turn Around Time for FCFS : ")
            Queue1.getAverageTurnAroundTime()



            print("Total waitin time for SJF : {}".format(Queue2.calculateWaitingTime()))
            print("Average Turn Around Time for SJF : {}".format(Queue2.getAverageTurnAroundTime()))


            time.sleep(5)
            
                        
            
    
    def work(self,Process):
        i=Process.burst_size
        print("Proces kuyruqu id:"+str(Process.GetQueue()))
        time.sleep(i)
        while i!=0:
            print("--")
            i-=1
        process=self.unit.pop()
        process.stopTurnAroundTime()
        

        if(process.GetQueue()==1):
            Queue1.setTurnAroundTime(process.getTurnAroundTime())
        elif(process.GetQueue()==2):
            Queue2.setTurnAroundTime(process.getTurnAroundTime())
        
        print("ID: :"+str(process.id))



TotalProb=1
Q1=0.5
Q2=TotalProb-Q1

def sendQueue(Process,QueID):
    
    if(QueID==1):
        print("Process "+str(Process.id)+" FCFS gidiyor")
        print("burst Size"+str(Process.burst_size))
        Process.SetQueue(1)#Queue1 için id=1
        Queue1.get(Process)

    elif(QueID==2):
        print("Process "+str(Process.id)+" SJF gidiyor")
        print("burst Size"+str(Process.burst_size))
        Process.SetQueue(2)#Queue1 için id=2
        Queue2.get(Process)
        

def createProcess(i,QueID):
        burstSize=2
        QueID=QueID
        Arr_time=i
        idim="id"+str(i)
        process=Process(burstSize,Arr_time,idim)
        Timer(Arr_time,sendQueue,[process,QueID]).start()
        return process
        
           
Cpu=CPU(1)
Queue1=FCFS()
Queue2=SJF()


#FCFS:1 #SJF:2

createProcess(1,1)
createProcess(2,1)
createProcess(3,1)
createProcess(3,2)

time.sleep(1)
while True:#display Queues size
    p=pt(target=Cpu.checkCpu())
    p.start()
    print("FCFS size:{}".format(Queue1.show()))
    print("SJF size:{}".format(Queue2.display()))
    
  
