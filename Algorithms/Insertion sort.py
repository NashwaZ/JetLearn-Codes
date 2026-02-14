l = [12,33,56,97,21,3,0,6]
1,
for i in range(len(l)):
    compare = l[i]
    pre = i - 1
    while pre >= 0 and compare < l[pre]:
        l[pre+1] = l[pre]
        pre -=1
    l[pre+1] = compare
    



