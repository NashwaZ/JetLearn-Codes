def fibonacci(a):
    if a == 0 or a == 1:
        return a
    else:
        return fibonacci(a-1) + fibonacci(a-2)

print(fibonacci(4))

def fact(b):
    if b == 1:
        return 1
    else:
        return b * fact(b-1)
    
print(fact(4))

def sum(c):
    if c == 0:
        return 0
    else:
        return c + sum(c-1)

print(sum(1))

def power(d,e):
    if e == 0:
        return 1
    elif e == 1:
        return d
    else:
        if e % 2 == 0:
            half_pow = power(d,e // 2)
            return half_pow * half_pow
        else:
            half_pow = power(d,e // 2)
            return d * half_pow * half_pow
print(power(2,2))

