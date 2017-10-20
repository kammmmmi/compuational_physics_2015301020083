# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import matplotlib.pyplot as plt
import math
v_x = [40]  
v_y = [0.]
x = [0.]
y = [1.8]
v_z = [0.]
z = [0.]
v_x2 = [40]
v_y2 = [0.]
v_z2 = [0.]
x2 = [0.]
y2 = [1.8]
z2 = [0.]
g = 9.8
dt = 0.01
end_time = 1
B_2m = 0.00004
S_0m = 0.00041
omega = math.pi * 200.0/3
def figure(x, y, z, v_x, v_y, v_z, omega):
    for i in range(int(end_time / dt)):
        if y[-1] >= 0:
            k_vx = v_x[i] - B_2m * v_x[i] * v_x[i]
            v_x.append(k_vx)
            k_x = x[i] + v_x[i] * dt
            x.append(k_x)
            k_vy = v_y[i] - g * dt
            v_y.append(k_vy)
            k_y = y[i] + v_y[i] * dt  
            y.append(k_y)
            k_vz = v_z[i] - S_0m * v_x[i] * omega
            v_z.append(k_vz)
            k_z = z[i] + v_z[i] * dt
            z.append(k_z)
            print x[-1], y[-1], z[-1]
        else:
            pass
    return None
plt.figure(figsize=(8,6)) 
figure(x, y, z, v_x, v_y, v_z, omega)
plt.plot(x,y,label="vertical deflection",color="green",linewidth=1) 
plt.plot(x,z,label="horizontal deflection",color="red",linewidth=1) 
plt.xlabel("x(m)") 
plt.ylabel("y/z(m)") 
plt.legend() 
plt.show() 
omega = math.pi * 10.0/3
plt.figure(figsize=(8,6)) 
figure(x2, y2, z2, v_x2, v_y2, v_z2, omega)
plt.plot(x2,y2,label="vertical deflection",color="green",linewidth=1) 
plt.plot(x2,z2,label="horizontal deflection",color="red",linewidth=1) 
plt.xlabel("x(m)") 
plt.ylabel("y/z(m)") 
plt.legend() 
plt.show() 
