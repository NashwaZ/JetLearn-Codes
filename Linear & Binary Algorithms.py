list = [21,34,67,2,54,1,34,7,3,87,45,8,4]

key = int(input("Enter no. to check: "))
'''
if key in list:
    print("yes, number is present")
else:
    print("number is not present")
'''
for l in list:
    if l == key:
        print("number is in list")
