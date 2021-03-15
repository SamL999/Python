import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([1,4,9,16,25,36,49,64])
z = np.array([1,2,3,6,9,15,24,39])

plt.figure(facecolor="lightgreen")


plt.plot(x,y,"b.--",linewidth=1.0)
plt.plot(x,z,"r.--",linewidth=1.0)

plt.xlim(0,8)
plt.ylim(0,70)
plt.title("Figure", size=24, loc="Center")
plt.xlabel("x-Value", size=16)
plt.ylabel("y-Value", size=16)


plt.show()