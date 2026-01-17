
import numpy as np
''''
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

'''
sample_array = np.array([1,3,4,5,8,2,13,4,3])
sample_array +=2
print(sample_array)

array1 = np.array([4,6,7,9,0,1])
array2 = np.array([2,4,3,1,7,9])

print(array1+array2)

#re-shaping 1d array into 2d array

ar = np.array([2,34,56,43,21,34,56,78,98,76,43,3,4,6,3,1])
ar2d = ar.reshape(2,8)
print(ar2d)
ar2d = ar.reshape(4,4)
print(ar2d)
ar2d = ar.reshape(8,2)
print(ar2d)
ar2d = ar.reshape(16,1)
print(ar2d)

array1d = np.array([23,45,7,8,5,2,1])

y = 2
d = 3

ans = y * array1d +3 
print(ans)

def solve_equation(x):
    y = 2 * x +3
    return y
ans_array = solve_equation(array1d)
print(ans_array)
