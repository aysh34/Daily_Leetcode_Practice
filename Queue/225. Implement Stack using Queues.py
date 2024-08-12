from collections import deque


class MyStack:
    # by following rules of queue, I have to implement stack
    def __init__(self):
        self.q1 = deque()  # main queue
        self.q2 = deque()  # helper queue

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            v1 = self.q1.popleft()
            self.q2.append(v1)
        popped = self.q1.popleft()
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return popped

    def top(self) -> int:
        while len(self.q1) > 1:
            v1 = self.q1.popleft()
            self.q2.append(v1)
        top = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self) -> bool:
        return len(self.q1) == 0


# def __init__(self):
#         self.q = deque()


#     def push(self, x: int) -> None:
#         self.q.append(x)

#     def pop(self) -> int:
#         for i in range(len(self.q) - 1):
#             self.push(self.q.popleft())
#         return self.q.popleft()
#     def top(self) -> int:
#         return self.q[-1]

#     def empty(self) -> bool:
#         return len(self.q) == 0
