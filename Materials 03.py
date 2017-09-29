import numpy as np 
import matplotlib.pyplot as plt
v = [0.]  
t = [0.] 
g = 9.8
dt = 0.1
end_time = 10
for i in range(int(end_time / dt)):
	k = v[i] - g * dt
	v.append(k)
	t.append(dt * (i + 1))     
	print（t[-1], v[-1]）
plt.figure(figsize=(8,6)) 
plt.plot(t,v,label="v(t)",color="red",linewidth=1)
plt.xlabel("t(s)") 
plt.ylabel("v(m/s)") 
plt.legend()  
plt.show() 
