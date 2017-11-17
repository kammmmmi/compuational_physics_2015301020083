# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x=[(2 + 2 ** 0.5) / 2.0]
y=[(2 ** 0.5) / 2.0]
vx, vy=0, 2
time,i,dt=0,0,0.001
sdt=0.00001
velocity=[4]
while time<=300:
    X = x[i] + vx * dt
    Y = y[i] + vy * dt
    if Y > 0 and Y < 2 ** 0.5:
        if X >= (2 + 2 ** 0.5) / 2.0:
            if Y > X - 2:
                x.append(X)
                y.append(Y)
                velocity.append(vx)
            else:
                x1 = x[i] + vx * sdt
                y1 = y[i] + vy * sdt
                if y1 > x1 - 2:
                    x.append(x1)
                    y.append(y1)
                    velocity.append(vx)
                else:
                    cash1 = vx              
                    cash2 = vy
                    vx = cash2
                    vy = cash1            
                    x.append(x[i] + vx * sdt)
                    y.append(y[i] + vy * sdt)
                    velocity.append(vx)
        if X < (2 + 2 ** 0.5) / 2.0:
            if Y < X:
                x.append(X)
                y.append(Y)
                velocity.append(vx)
            else:
                x2 = x[i] + vx * sdt
                y2 = y[i] + vy*sdt
                if y2 < x2:
                    x.append(x2)
                    y.append(y2)
                    velocity.append(vx)
                else:
                    cash3 = vx
                    char4 = vy
                    vx = vy
                    vy = vx
                    x.append(x[i]+vx*sdt)
                    y.append(y[i]+vy*sdt)
                    velocity.append(vx)
    if Y >= 2 ** 0.5:
        x4 = x[i] + vx * sdt
        y4 = y[i] + vy * sdt
        if y4 < 2 ** 0.5:
            x.append(x4)
            y.append(y4)
            velocity.append(vx)
        else:   
            vy=-vy
            x.append(x[i]+vx*sdt)
            y.append(y[i]+vy*sdt)
            velocity.append(vx)
    if Y <= 0:
        x3=x[i]+vx*sdt
        y3=y[i]+vy*sdt
        if y3 > 0:
            x.append(x3)
            y.append(y3)
            velocity.append(vx)
        else:   
            vy=-vy
            x.append(x[i]+vx*sdt)
            y.append(y[i]+vy*sdt)
            velocity.append(vx)
    time=time+dt
    i=i+1
plt.figure(figsize=(16,5.5))
subplot(1,2,1)
plt.title("vx0=0,vy0=2")
plt.xlabel("x")
plt.ylabel("y")
plt.xticks([0,0.5,1,1.5,2,2.5,3,3.5])
plt.yticks([0,0.5,1,1.5])
plt.xlim(0, 3.5)
plt.ylim(0, 2)
plt.plot([0, 2 ** 0.5],[0, 2 ** 0.5],color="blue",label="rhombus",linewidth=2)
plt.plot([2 ** 0.5, 2 + 2 ** 0.5],[2 ** 0.5, 2 ** 0.5],color="blue",linewidth=2)
plt.plot([2 + 2 ** 0.5, 2],[2 ** 0.5, 0],color="blue",linewidth=2)
plt.plot([0, 2],[0, 0],color="blue",linewidth=2)
plt.plot(x,y,label="trajectory",color="red")
plt.scatter((2 + 2 ** 0.5) / 2.0,(2 ** 0.5) / 2.0,color="black",alpha=1,linewidth=4,label="initial")
plt.legend()
subplot(1,2,2)
plt.xlabel("x")
plt.ylabel("vx")
for i in range(1000):
    if 1000*i<=len(x):
        plt.scatter(x[1000*i],velocity[1000*i])
plt.show()
