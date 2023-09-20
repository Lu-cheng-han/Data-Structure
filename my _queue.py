

class MyQueue:

    stack1 = []
    stack2 = []

    def push(self, val : int):
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(val)
    
    def pop(self):
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()    
    
    def peek(self):
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return 1
        else:
            return 0

if __name__ == "__main__":
    my_queue = MyQueue()

    my_queue.push(12)
    my_queue.push(13)
    my_queue.push(565)
    while not my_queue.empty():
        print(my_queue.pop())