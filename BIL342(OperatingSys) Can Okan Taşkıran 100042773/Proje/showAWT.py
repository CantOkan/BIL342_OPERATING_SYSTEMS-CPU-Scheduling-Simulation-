import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style



fig=plt.figure()

ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

def animate(i):
    grap_data=open("ATT1.txt","r").read()
    grap_data2=open("ATT2.txt","r").read()
    grap_data3=open("WT1.txt","r").read()
    grap_data4=open("WT2.txt","r").read()

    lines=grap_data.split('\n')
    lines2=grap_data2.split('\n')
    lines3=grap_data3.split('\n')
    lines4=grap_data4.split('\n')

    xs=[]
    ys=[]

    xs2=[]
    ys2=[]


    xs3=[]
    ys3=[]

    xs4=[]
    ys4=[]
    
    for line in lines:
        if len(line)>1:
            x,y=line.split(",")
            xs.append(y)
            ys.append(x)

    for satir in lines2:
       if len(lines2)>1:
            x,y=satir.split(",")
            xs2.append(y)
            ys2.append(x)


    for lines in lines3:
       if len(lines)>1:
            x,y=lines.split(",")
            xs3.append(y)
            ys3.append(x)


    for satir3 in lines4:
        if len(lines4)>1:
            x,y=satir3.split(",")
            xs4.append(y)
            ys4.append(x)
            



   
    ax1.set_title("FCFS(R) and SJF(B)")
    xs = list(map(float, xs))
    ys = list(map(float, ys))
    xs2= list(map(float, xs2))
    ys2= list(map(float, ys2))

    ax1.set_ylabel("Average Waiting time")
    ax1.plot(xs,ys,'r')
    ax1.plot(xs2,ys2,'b')


    xs3 = list(map(float, xs3))
    ys3 = list(map(float, ys3))
    xs4= list(map(float, xs4))
    ys4= list(map(float, ys4))


    ax2.set_title("FCFS(R) and SJF(B)")    
    ax2.set_ylabel("Average TurnAround Time")
    ax2.plot(xs3,ys3,'r')
    ax2.plot(xs4,ys4,'b')



animate=animation.FuncAnimation(fig,animate,interval=1000)

plt.show()