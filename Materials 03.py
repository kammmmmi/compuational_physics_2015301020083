import numpy as a 

import matplotlib.pyplot as b

v = [0.]  
t = [0.] 
g = 9.8
dt = 0.1
end_time = 10

for i in range(int(end_time / dt)):

	k = v[i] - g * dt

	v.append(k)

	t.append(dt * (i + 1))     

	print t[-1], v[-1]

b.figure(figsize=(8,6)) 

b.plot(t,x,label="x(t)",color="red",linewidth=1)

b.xlabel("t(s)") 

b.ylabel("v(m/s)") 

b.legend()  

b.show() 
