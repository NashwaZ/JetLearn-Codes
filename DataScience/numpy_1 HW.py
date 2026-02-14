import numpy as np

rows = int(input("Enter the no. of rows for your matrices: "))
columns = int(input("Enter the no. of columns for your matrices: "))

matrix1 = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        element = int(input(f"Enter a number for row {row}, column {column}: "))
        current_row.append(element)
    matrix1.append(current_row)

array1 = np.array(matrix1)
print(f"This is Matrix 1: {array1}")

matrix2 = []
for row in range(rows):
    current_row = []

    for column in range(columns):
        element = int(input(f"Enter a number for row {row}, column {column}: "))
        current_row.append(element)
    matrix2.append(current_row)

array2 = np.array(matrix2)
print(f"This is Matrix 2: {array2}")

operation = int(input("Choose your operation: 1 = + , 2 = - "))

if operation == 1:
    print(f"{matrix1} + {matrix2} = {array1+array2}")
elif operation == 2:
    print(f"{matrix1} - {matrix2} = {array1-array2}")
else:
    print("ERROR - ensure you enter 1 or 2 to perform an operation")