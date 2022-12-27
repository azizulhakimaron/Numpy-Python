import numpy as np
arr1=np.arange(1,11)
print(arr1)
print(arr1>5)
x=arr1>5
print(arr1[x])
odd=arr1%2==0
print(arr1[odd])
even=arr1%2==1
print(arr1[even])