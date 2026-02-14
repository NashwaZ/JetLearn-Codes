class Queue():
    def __init__(self, max):
        self.queue = [None] * max
        self.head = 0
        self.tail = 0
        self.max = max
        self.available = max
    '''
    def enqueue(self, data):
        self.queue.append(data)
        self.tail +=1
        print(f"The data: {data} has been added to the queue")
    '''
    def enqueue(self, data): 
        if self.available == 0:
            print("Queue is full")
        else:
            self.queue[self.tail] = data
            self.tail = (self.tail +1) % self.max
            self.available - 1


    ''' def dequeue(self):
        if len(self.max) > 0:
            removed = self.queue.pop(self.head)
            self.head +=1
            print(f"{removed} was removed was the list")'''

    def dequeue(self):
        if self.available == self.max:
            print("cannot remove any more items")
        else:
            self.queue[self.head] = None
            self.head = [self.head +1] % self.max
            self.available + 1

    def display(self):
        print(self.queue)

    
    def get_head(self):
        print(self.queue[self.head])
    def get_tail(self):
        print(self.queue[self.tail])




