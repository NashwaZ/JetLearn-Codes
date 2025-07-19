class Queue():
    def __init__(self, max):
        self.queue = [None] * max
        self.max = max
        self.head = 0
        self.tail = 0
    '''
    def enqueue(self, data):
        self.queue.append(data)
        self.tail +=1
        print(f"The data: {data} has been added to the queue")
    '''

    def dequeue(self):
        if len(self.max) > 0:
            removed = self.queue.pop(self.head)
            self.head +=1
            print(f"{removed} was removed was the list")
    def display(self):
        print(self.queue)
    


print([None]*5)