class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # fix sized
        self.front = 0
        self.rear = -1
        self.maxSize = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.queue[self.rear] = value
            self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.maxSize
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():  # If the queue is empty, return -1
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():  # If the queue is empty
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxSize
