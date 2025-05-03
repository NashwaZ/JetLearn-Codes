'''
var = [1,4,2,6,8,53,7]

var.sort(reverse=False)
print(var)

for n in range(len(var)):
    for i in range(n,len(var)):
        if var[n] > var[i]:
            var[n], var[i] = var[i], var[n]
print(var)


a = [5,3,8,4,2]

for i in range(len(a)):
    min = 100000000
    min_location = -1
    for j in range(i,len(a)):
        if min > a[j]:
            min = a[j]
            min_location = j
            a[i], a[j] = a[j], a[i]
print(a)


a = [5,3,8,4,2]

for i in range(len(a)):
    max = -10000000
    max_location = -1
    for j in range(i,len(a)):
        if max < a[j]:
            max = a[j]
            max_location = j
            a[i], a[j] = a[j], a[i]
print(a)


l = [289,4,378,42,1,4]

is_swapping = True
print(l)

while is_swapping:
    is_swapping = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            is_swapping = True
print(l)
'''

l = [289,4,378,42,1,4]

is_swapping = True
print(l)

while is_swapping:
    is_swapping = False
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            is_swapping = True
print(l)


