import numpy as np
np.random.seed(100)
arr1=np.array([1,7,3,9,5])
print(arr1[1])
print(arr1[-3])
print(arr1[1:4])
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix1[1][0])
print(matrix1[1,0])
print(matrix1[:2, :2])
print(matrix1[1:,1:])
matrix2=np.random.randint(1,101,25).reshape(5,5)
print(matrix2)
print(matrix2[2:6,2:6])

