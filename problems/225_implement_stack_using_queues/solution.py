from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        result = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return result

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        result = self.queue1.popleft()
        self.queue2.append(result)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return result

    def empty(self) -> bool:
        return not self.queue1


obj = MyStack()
obj.push(1)
obj.push(2)
top_output = obj.top()
pop_output = obj.pop()
empty_output = obj.empty()

print(f'peek operation output (should be 2): {top_output}')
print(f'pop operation output (should be 2): {pop_output}')
print(f'empty operation output (should be False): {empty_output}')
