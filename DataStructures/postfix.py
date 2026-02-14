
class Stack():
    def __init__(self):
        self.stack_list = []
    def push(self,data):
        self.stack_list.append(data)
    def pop(self):
        return self.stack_list.pop()
    def top(self):
        if len(self.stack_list) > 0:
            return self.stack_list[-1]
    def is_empty(self):
        return len(self.stack_list) == 0
        

infix = input("Enter an infix expression: ")

def infix_to_postfix(infix):
    stack = Stack()
    postfix = ""
    precedence = {"^":3, "*":2, "/":2, "-":1, "+":1}
    for ch in infix:
        if "A" <= ch <= "Z" or "a" <= ch <= "z" or "0" <= ch <= "9" :
            postfix += ch
        elif ch in precedence:
            while not stack.is_empty() and precedence[ch] <= precedence[stack.top()]:
                postfix += stack.pop() 
            stack.push(ch)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix


final = infix_to_postfix(infix)
print("Postfix: " + final)


