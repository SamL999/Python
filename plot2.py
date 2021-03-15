import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = x * 2

# plt.figure(figsize=(16,9), facecolor="lightblue")
plt.figure(dpi=100)

plt.plot(x,y,"r.", label="Y=X*2")

for i in range(len(x)):
    i = i+1
    j = i*2
    plt.text(i+0.06,j,j)

plt.legend()

plt.show()


