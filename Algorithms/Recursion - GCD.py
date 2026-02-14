
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


print("The GCD is:", gcd(x, y))

