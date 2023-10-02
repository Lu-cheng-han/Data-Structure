from queue import Queue
class MyStack:

    def __init__(self) -> None:
        self.queue = Queue()

    def push(self,val):
        self.queue.put(val)

    def pop(self):
        data = []
        while self.queue.qsize() != 1:
            data.append(self.queue.get())
        last_data = self.queue.get()
        for i in data:
            self.queue.put(i)
        return last_data

    def empty(self):
        if self.queue.empty():
            return True
        else:
            return False

    def top(self):
        last_data =  self.pop()
        self.queue.put(last_data)
        return last_data
    
    def size(self):
        return self.queue.qsize()

if __name__ == "__main__":
    my_stack = MyStack()
    my_stack.push(55)
    my_stack.push(44)
    my_stack.push(33)
    my_stack.push(22)
    print("my_stack size", my_stack.size())
    print("pop",my_stack.pop())
    print("my_stack size", my_stack.size())
    print("pop",my_stack.top())


