import matplotlib.pyplot as plt



#from matplotlib import style

#plt.style.use("ggplot")


fig=plt.figure()

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

grap_data=open("PRO.txt","r").read()
lines=grap_data.split('\n')

grap_data2=open("fileQueueLength.txt","r").read()
lines2=grap_data2.split('\n')

grap_data3=open("AVGQueueLength.txt","r").read()
lines3=grap_data3.split('\n')


xs=[]
ys=[]

xs2=[]



xs3=[]
xs4=[]
ys3=[]

zs=[]
ws=[]
ys4=[]


for line in lines:
    if len(line)>1:
        x,x2,y=line.split(",")
        xs.append(x)
        xs2.append(x2)
        ys.append(y)

for line in lines2:
    if len(line)>1:
        x,x2,y=line.split(",")
        xs3.append(x)
        xs4.append(x2)
        ys3.append(y)


for line in lines3:
    if len(line)>1:
        x,x2,y=line.split(",")
        zs.append(x)
        ws.append(x2)
        ys4.append(y)




xs = list(map(float, xs))
ys = list(map(float, ys))
xs2= list(map(float, xs2))



ax1.set_title("Priorty")


#ax1.set_ylim([0,1])
ax1.plot(ys,xs,'r')
ax1.plot(ys,xs2,'b')

ax1.set_ylabel("FCFS(R) SJF(B)")

ax2.set_title("FCFS(R) SJF(B)")
ax2.set_ylabel("Priority Oranı")
ax2.set_xlabel("p1/p2")
ax2.plot(xs,xs2,'r')


ax3.set_title("QUEUE LENGTH")
ax3.set_ylabel("FCFS(R) SJF(B)")

xs3 = list(map(float, xs3))
ys3 = list(map(float, ys3))
xs4= list(map(float, xs4))


ax3.plot(ys3,xs3,'r')
ax3.plot(ys3,xs4,'b')


zs = list(map(float, zs))
ws = list(map(float, ws))
ys4 = list(map(float, ys4))

ax4.plot(ys4,zs,'r')
ax4.plot(ys4,ws,'b')
ax4.set_xlabel("AVG. Queue Len.")

plt.show()