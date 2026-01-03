import numpy as np

#creating arrays

l1 = [12,43,16,45,75,65,98,123,45,9]
l2 = ['cat','dog','lion','ball']
         
#1 dimensional array
one_d_ar = np.array(l1)
print(f"list = {l1}")
print(f"array = {one_d_ar}")
print(type(l1))
print(type(one_d_ar))

one_d_ar2 = np.array(l2)
print(one_d_ar2)
print(type(one_d_ar2))

#array slicing [starting : ending : steps]
print(one_d_ar[:])
print(one_d_ar2[:3])
print(one_d_ar[::2])
print(one_d_ar[::3])
print(one_d_ar[::-1])

#2 dimensional arrays
l12d = [[43,54,5], [23,48,7], [12,32,45], [32,18,65]] #the number of elements have to be the same 

print(one_d_ar.shape)
#print(l12d.shape)


two_d_ar = np.array(l12d)
print(two_d_ar)

# 2d array slicing [row starting index : row ending index, column starting index : column ending index]

print(two_d_ar[:])
print(two_d_ar[1:3, :])
print(two_d_ar[1:, 1:])