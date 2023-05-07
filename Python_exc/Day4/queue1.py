
class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: The queue is empty.")
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
q= Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.insert(16)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

