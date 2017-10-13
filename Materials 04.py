# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import math
v_x = [0.]  
v_y = [0.]
x = [0.]
y = [0.]
v_x2 = [0.]  
v_y2 = [0.]
x2 = [0.]
y2 = [0.]
v_x3 = [0.]  
v_y3 = [0.]
x3 = [0.]
y3 = [0.]
v_x4 = [0.]  
v_y4 = [0.]
x4 = [0.]
y4 = [0.]
v_x5 = [0.]  
v_y5 = [0.]
x5 = [0.]
y5 = [0.]
v_x6 = [0.]  
v_y6 = [0.]
x6 = [0.]
y6 = [0.]
g = 9.8
dt = 0.1
end_time = 1000
V = 700
def sin(x):
    math.sin(x * math.pi/180)
    return math.sin(x * math.pi/180)
def cos(x):
    math.cos(x * math.pi/180)
    return math.cos(x * math.pi/180)
def figure(x, y, v_x, v_y, theta):
    v_x.append(V * cos(theta))
    v_y.append(V * sin(theta))
    for i in range(int(end_time / dt)):
        if y[-1] >= 0:
            k_vx = v_x[i]
            k_x = x[i] + v_x[i] * dt
            v_x.append(k_vx)
            x.append(k_x)
            k_vy = v_y[i] - g * dt
            k_y = y[i] + v_y[i] * dt
            v_y.append(k_vy)
            y.append(k_y)     
            print x[-1], y[-1]
        else:
            pass
    v_x = [0.]  
    v_y = [0.]
    x = [0.]
    y = [0.]
    return None
plt.figure(figsize=(8,6)) 
figure(x, y, v_x, v_y, 30)
plt.plot(x,y,label="30",color="green",linewidth=1) 
figure(x2, y2, v_x2, v_y2, 35)
plt.plot(x2,y2,label="35",color="red",linewidth=1)
figure(x3, y3, v_x3, v_y3, 40)
plt.plot(x3,y3,label="40",color="black",linewidth=1)
figure(x4, y4, v_x4, v_y4, 45)
plt.plot(x4,y4,label="45",color="brown",linewidth=1)
figure(x5, y5, v_x5, v_y5, 50)
plt.plot(x5,y5,label="50",color="yellow",linewidth=1)
figure(x6, y6, v_x6, v_y6, 55)
plt.plot(x6,y6,label="55",color="gray",linewidth=1)
plt.xlabel("x(m)") 
plt.ylabel("y(m)") 
plt.legend() 
plt.show() 
