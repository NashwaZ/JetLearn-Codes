class Stack():
    def __init__(self,limit):
        self.stack_list = []
        self.limit = limit
    def push(self,data):
        if len(self.stack_list) < self.limit:
            self.stack_list.append(data)
            print("data added to stack")
        else:
            print(f"cannot add {data} as Stack is full")
    def pop(self):
        if len(self.stack_list) > 0:
            last_index = len(self.stack_list) - 1
            last_item = self.stack_list[last_index]
            print("popped", last_item)
            self.stack_list.remove(last_item)
        else:
            print("Stack is empty")

    def display(self):
        print("stack:",self.stack_list)

    def top(self):
        if len(self.stack_list) == 0:
            return -1
        else:
            return len(self.stack_list) -1
    
book = Stack(3)
book.push("car")
book.display()
book.pop()
book.pop()
book.push("red")
book.push("bike")
book.push("glass")
book.push("mouse")
book.display()

x = book.top()
if x == -1:
    print("Stack is empty")
else:
    print(f"There are {x+1} items in the stack")


        


