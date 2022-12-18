import numpy as np
arr=np.random.randint(1,100,20)
print(arr)
print(arr.ndim)#To check dimention
print(arr.shape)#to check elements
x=arr.reshape(2,10)
print(x)
print(x.shape)
print(x.ndim)
y=x.reshape(20)
print(y)
z=arr.reshape(2,2,5)
print(z)
z1=arr.reshape(5,-1)#(5X4)=20
print(z1)
z2=arr.reshape(-1,5)#(5X4)=20
print(z2)