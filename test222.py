import numpy as np

x = np.random.randint(1,21,20)
y = x.reshape(5,4)
z = y[np.ix_([0,-1],[0,-1])]

print ("隨機正整數 ： ",x)
print ("X矩陣內容 : \n",y)
print ("最大 : ",np.min(x))
print ("最小 : ",np.max(x))
print ("平均 : ",np.mean(x))
print ("總和 : ",np.sum(x))
print ("標準差 : ",np.std(x))
print ("四個角落元素 : \n",z)

