import numpy as np

equation = input("Enter the type of equation (Linear / Quadratic): ").lower()

if equation == 'linear':
    a = int(input("Enter 1st coefficient: "))
    b = int(input("Enter 2nd coefficient: "))
    
    print(f"Results for Linear Equation: y = {a}x + {b}")
    for x in range(11):
        ans = a * x + b
        print(f"x = {x}, Answer = {ans}")

elif equation == 'quadratic':
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))
    
    print(f"Results for Quadratic Equation: y = {a}x^2 + {b}x + {c}")
    for x in range(11):
        ans = a * (x**2) + b * x + c
        print(f"x = {x}, Answer = {ans}")







