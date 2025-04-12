'''

list = [21,34,67,2,54,1,34,7,3,87,45,8,4]

key = int(input("Enter no. to check: "))

if key in list:
    print("yes, number is present")
else:
    print("number is not present")

for l in list:
    if l == key:
        print("number is in list")


sorted = [1,2,3,4,12,23,24,25,45,46,56,67,78,90]

key = int(input("Enter number: "))

low = 0
high = len(sorted) - 1

while low <= high:
    middle = (low+high) // 2
    if sorted[middle] == key:
        print(f"{key} is in the list")
        break
    elif sorted[middle] < key:
        low = middle + 1
    else:
        high = middle - 1
else:
    print("number is not present")

'''
    
#12/04/2025 Binary Search HW

sorted_list = [1, 4, 10, 12, 54, 67, 77, 79, 87, 90, 93, 99, 101, 231]

key = int(input("Enter number: "))

low = 0
high = len(sorted_list) - 1

while low <= high:
    middle = (low + high) // 2
    if sorted_list[middle] == key:
        print(f"{key} is in the list at index {middle}")
        break
    elif sorted_list[middle] < key:
        low = middle + 1
    else:
        high = middle - 1
else:
    print("Number is not present in the list")
    

    