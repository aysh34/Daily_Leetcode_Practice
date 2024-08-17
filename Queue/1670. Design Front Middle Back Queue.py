from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _rebalance(self):
        # Rebalance the two deques to ensure their sizes are balanced
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self._rebalance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self._rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) == len(self.back):
            val = self.front.pop()
        else:
            val = self.front.pop()
        self._rebalance()
        return val

    def popBack(self) -> int:
        if not self.back and not self.front:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        self._rebalance()
        return val

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()