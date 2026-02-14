open_bracket = ["[","(","{"]
close_bracket = ["]",")","}"]

user = input("Enter an expression using brackets: ")

def check_exp(user):
    stack = []
    for ch in user:
        if ch in open_bracket:
            stack.append(ch)
        elif ch in close_bracket:
            cindex = close_bracket.index(ch)
            if len(stack) > 0 and open_bracket[cindex] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "Unbalanced expression"
            
    if len(stack) == 0:
        return 'Balanced expression'
    else:
        return 'Unbalanced expression'

x = check_exp(user)
print(x)
