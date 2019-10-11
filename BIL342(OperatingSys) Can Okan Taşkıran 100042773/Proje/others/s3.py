#priorty degerini anlık adetten yararlanarak atıyorum

import random
import queue
from threading import Timer
import time
from multiprocessing import Process as pt
import numpy

text_file=open("deneme.txt","w")
text_file2=open("deneme2.txt","w")

text_file3=open("ATT1.txt","w")
text_file4=open("ATT2.txt","w")

text_filePR=open("PRO.txt","w")

start=time.time()
status=True

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
         if(self.adet==0):
            return 0
         else:
            return self.totalWaiting/self.adet

    def setTurnAroundTime(self,zaman):
        print("TTA: "+str(zaman))
        self.totalTTA+=zaman

    def getAverageTurnAroundTime(self):
         if(self.adet==0):
            return 0
         else:
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
         if(self.adet==0):
            return 0
         else:
            return self.totalWaiting/self.adet
    

    def setTurnAroundTime(self,zaman):
        print("TTA: "+str(zaman))
        self.totalTTA+=zaman

    def getAverageTurnAroundTime(self):
        if(self.adet==0):
            return 0
        else:
            return self.totalTTA/self.adet

class CPU(object):
    unit=list()

    TotalProb=1
    Queue1prob=0.6
    Queue2prob=TotalProb-Queue1prob

    countofCreatedProcess=0
    def __init__(self,core):
        self.core=core
    
    def setCount(self,i):
        self.countofCreatedProcess=i


    def checkCpu(self):
        x=random.uniform(0,1)
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

        elif(Queue1.show()==0 and Queue2.display()==0 and self.countofCreatedProcess==(Queue1.adet+Queue2.adet)):
            print("NOW you're in idle situation")
            print("FCFS adet: {}".format(Queue1.count()))
            print("SJF adet: {}".format(Queue2.count()))

            now=int(time.time()-start)
            minute = now / 60
            sec=now % 60

            #Waiting_Time
            wt1=Queue1.calculateWaitingTime()
            wt1=float("{0:.2f}".format(wt1))#noktadan sonra iki satır
            wt2=Queue2.calculateWaitingTime()

            print("Average waitin time for SJF : {}".format(Queue2.calculateWaitingTime()))
            print("Average waitin time for FCFS : {}".format(Queue1.calculateWaitingTime()))
            
            text_file.write(str(wt1)+","+str(sec)+"\n")
            text_file2.write(str(wt2)+","+str(sec)+"\n")

            
            
       

            ##Average Turn Around Time
            tta1=Queue1.getAverageTurnAroundTime()
            tta1=float("{0:.2f}".format(tta1))
            tta2=Queue2.getAverageTurnAroundTime()
            tta2=float("{0:.2f}".format(tta2))

            
            print("Average Turn Around Time for FCFS : {}".format(Queue1.getAverageTurnAroundTime()))
            print("Average Turn Around Time for SJF : {}".format(Queue2.getAverageTurnAroundTime()))

            text_file3.write(str(tta1)+","+str(now)+"\n")
            text_file4.write(str(tta2)+","+str(now)+"\n")

            
            """Kuyruğu sıfırla
            totalTTA,totalWaiting,adet=0
            
            """

            #text_filePR.write()
            print("QUEUE1 prob:"+str(self.Queue1prob))
            
            if(Queue1.adet!=0 and Queue2.adet!=0):
                ProcessAdet=Queue1.adet+Queue2.adet
                Queue1oran=Queue1.adet/ProcessAdet
                Queue2oran=1-Queue1oran
                print("Q2 Oranı:"+str(Queue2oran))
                print("Q1 Oranı:"+str(Queue1oran))
                if(Queue1oran>self.Queue1prob): #Adet'e gore Proiority Ayarlama
                                                #decrease the Q1 prob
                    fark=numpy.abs(Queue1oran-self.Queue1prob)
                    degisim=fark
                    self.Queue1prob=self.Queue1prob+degisim
                    print("degisim :"+str(degisim))
                elif(Queue1oran<self.Queue1prob):
                    fark=numpy.abs(self.Queue1prob-Queue1oran)
                    degisim=fark
                    self.Queue1prob=self.Queue1prob-degisim
                    print("degisim:"+str(degisim))

            Queue1.totalTTA=0
            Queue1.totalWaiting=0
            Queue1.adet=0

            Queue2.totalTTA=0
            Queue2.totalWaiting=0
            Queue2.adet=0
            ask()

                               
    
    def work(self,Process):
        i=int(Process.burst_size)
        print("Proces kuyruqu id:"+str(Process.GetQueue()))
        
        time.sleep(i)
        while i!=0:
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

def sendQueue(Process):
    z=random.uniform(0,1)
    
    if(Q1>z):
        print("Process "+str(Process.id)+" FCFS gidiyor")
        Process.SetQueue(1)#Queue1 için id=1
        Queue1.get(Process)
    elif(z>=Q2):
        print("Process "+str(Process.id)+" SJF gidiyor")
        Process.SetQueue(2)#Queue2 için id=2
        Queue2.get(Process)
        

def createProcess():
     burstSize=numpy.random.exponential()
     print("EXPONENTAİL burst Size:"+str(burstSize))
     Arr_time=numpy.random.exponential()
     print("Arrive time "+str(Arr_time))
     idim="id"+str(Arr_time)
     process=Process(burstSize,Arr_time,idim)
     Timer(Arr_time,sendQueue,[process]).start()
     return process
    
       
        
        
           
Cpu=CPU(1)
Queue1=FCFS()
Queue2=SJF()



def ask():
    x=input("Would you like to create process: (press:x)")
    if(x=="x"):
        processler()
        time.sleep(1)
           


def processler():
    x=random.randint(5,20)
    Cpu.setCount(x)
    print("Adet process üretileck"+str(x))
    for i in range(0,x):
        createProcess()




while status:#display Queues size
    p=pt(target=Cpu.checkCpu())
    p.start()
   
    Cpu.checkCpu()
  
