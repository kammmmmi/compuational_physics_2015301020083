# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import matplotlib.pyplot as plt
x = [1.]  
y = [0.] 
z = [0.]
dt = 0.0001
end_time = 100
r = 25
sigma = 10
b = 8.0/3
for i in range(int(end_time / dt)):
    dx = sigma * (y[-1] - x[-1]) * dt
    kx = x[-1] + dx
    dy = (-x[-1] * z[-1] + r * x[-1] - y[-1]) * dt
    ky = y[-1] + dy
    dz = (x[-1] * y[-1] - b * z[-1]) * dt
    kz = z[-1] + dz
    x.append(kx)
    y.append(ky)
    z.append(kz)
    print x[-1], y[-1], z[-1]
plt.figure(figsize=(8,6)) 
plt.plot(x,z,label="z versus x",color="red",linewidth=1)
plt.xlabel("x") 
plt.ylabel("z") 
plt.legend()  
plt.show() 
--------------------------------------------------------------
