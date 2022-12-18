import numpy as np
nums=[1,2,3],[4,5,6.0]#2D matrix
nums1=[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]#3D matrix
nums=np.array(nums)
nums1=np.array(nums1)
print(nums)
print(nums1)
print(nums.ndim,nums1.ndim)#ndim to check dimention
print(nums.shape)
print(nums.dtype)