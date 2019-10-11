import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style


style.use('fivethirtyeight')

fig=plt.figure()

ax1=fig.add_subplot(1,2,1)


def animate(i):
    grap_data=open("deneme3.txt","r").read()
    grap_data2=open("deneme4.txt","r").read()
    lines=grap_data.split('\n')
    lines2=grap_data2.split('\n')
    xs=[]
    ys=[]

    xs2=[]
    ys2=[]
    
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

    plt.ylabel("data")
    plt.xlabel("time")
    plt.plot(xs2,ys2,'b')
    plt.plot(xs,ys,'r')
    


animate=animation.FuncAnimation(fig,animate,interval=1000)

plt.show()