
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


def is_balanced(expression):
    stack = Stack()
    open_list = ["[","{","("]
    close_list = ["]","}",")"]

    for char in expression:
        if char in open_list:
            stack.push(char)
        elif char in close_list:
            index = close_list.index(char)
            if not stack.is_empty() and stack.top() == open_list[index]:
                stack.pop()
            else:
                return "unbalanced"

    return "balanced" if stack.is_empty() else "unbalanced"

expr = input("Enter an expression: ")
print(is_balanced(expr))