import numpy as np
import matplotlib.pyplot as plt

"""
x = np.arange(0,5,0.1)

plt.plot(x,x,"r-")
plt.plot(x,x**2.5,"c:")
plt.plot(x,x**3,"y.") """

plt.rcParams["font.family"]="Microsoft Yahei"

x = np.array([-2,3,4,5,6.5])
y = x ** 2

plt.plot(x,y,"b--")
plt.plot([-1,2,4],[2,-9,20],"r--")

plt.xlim(-3,8)
plt.ylim(-10,50)
# plt.xticks(np.arange(5))
# plt.yticks(np.arange(5))
plt.title("Y = X的2次方", size=16, loc="Center")
plt.xlabel("X 軸", size=14)
plt.ylabel("Y 軸", size=14, rotation=0, ha="right")

# plt.grid()

plt.minorticks_on()

plt.show()

