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

class Job_Queue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,data):
        self.stack1.push(data)
    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            print("No jobs to cancel")
        elif self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            print(f"The '{self.stack2.pop()}' job was canceled")
        else:
            print(f"The '{self.stack2.pop()}' job was canceled")
            

    def front(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            return self.stack2.top()
    def rear(self):
        if not self.stack1.is_empty():
            return self.stack1.top()
        
    def size(self):
        return len(self.stack1.stack_list) + len(self.stack2.stack_list)


scheduler = Job_Queue()
scheduler.enqueue("house")
scheduler.enqueue("car")
print("Next job to print:", scheduler.front())
print("Most recent job:", scheduler.rear())

scheduler.dequeue()
print(f"Number of prints: {scheduler.size()}")

scheduler.enqueue("ball")
print(f"Added {scheduler.rear()} to the queue")

scheduler.dequeue()
scheduler.dequeue()
scheduler.dequeue()
