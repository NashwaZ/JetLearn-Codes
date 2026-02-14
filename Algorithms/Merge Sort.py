l = [23,43,65,2,12,6,98,30,24,2,21]
print(l)

def merge_sort(l):
    if len(l) <= 1:
        return l
    #div arrays into two halves
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:]) 
    return merge(left, right)


def merge(left,right):
    sortedl = []
    i = 0 #left index
    j = 0 #right index

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedl.append(left[i])
            i +=1
        else:
            sortedl.append(right[j])
            j +=1
    
    #adding remaining elements
    sortedl.extend(left[i:])
    sortedl.extend(right[j:])
    return sortedl

sortedl = merge_sort(l)
print(sortedl)

    

