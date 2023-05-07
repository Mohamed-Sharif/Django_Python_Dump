import json


class Queue:
    queues = {}
    def __init__(self, name, size):
        self.queue = []
        self.name = name
        self.size = size
        if name in Queue.queues:
            raise ValueError("A queue with this name already exists.")
        else:
            Queue.queues[name] = self

    @classmethod
    def save(cls, filename):
        queues_dict = {}
        for name, queue in cls.queues.items():
            queues_dict[name] = {
                "size": queue.size,
                "elements": queue.queue
            }
        with open(filename, "w") as f:
            json.dump(queues_dict, f)

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as f:
            queues_dict = json.load(f)
        cls.queues = {}
        for name, data in queues_dict.items():
            queue = Queue(name, data["size"])
            for element in data["elements"]:
                queue.insert(element)



    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException("Queue is full.")
        else:
            self.queue.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: The queue is empty.")
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

class QueueOutOfRangeException(Exception):
    pass


q = Queue("my_queue", 3)

q.insert(1)
q.insert(2)
q.insert(3)

try:
    q.insert(4)
except QueueOutOfRangeException:
    print("The queue is full.")

print(q.pop()) 
print(q.pop())

print(q.pop())  

Queue.save("queues.json")

q2 = Queue("my_queue2", 3)

Queue.load("queues.json")

print(q2.pop()) 
