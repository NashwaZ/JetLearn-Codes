user = input("Enter an Expression: ")
a = user[0]
operator = user[1]
b = user[2]

print(f"infix: {user}, postfix: {a + b + operator}, prefix: {operator + a + b}")

