import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style


style.use('fivethirtyeight')

fig=plt.figure()

ax1=fig.add_subplot(1,2,1)


def animate(i):
    grap_data=open("deneme.txt","r").read()
    grap_data2=open("deneme2.txt","r").read()
    lines=grap_data.split('\n')
    lines2=grap_data2.split('\n')
    xs=[]
    ys=[]

    xs2=[]
    ys2=[]
    
    for line in lines:
        if len(line)>1:
            x,y=line.split(",")
            xs.append(x)
            ys.append(y)

    for satir in lines2:
       if len(lines2)>1:
            x,y=satir.split(",")
            xs2.append(x)
            ys2.append(y)

    plt.ylabel("data")
    plt.xlabel("time")
    plt.plot(xs,ys,'r')
    plt.plot(xs2,ys2,'b')


animate=animation.FuncAnimation(fig,animate,interval=1000)

plt.show()