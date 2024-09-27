class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


obj = MyQueue()
obj.push(1)
obj.push(2)
peek_output = obj.peek()
pop_output = obj.pop()
empty_output = obj.empty()

print(f'peek operation output (should be 1): {peek_output}')
print(f'pop operation output (should be 1): {pop_output}')
print(f'empty operation output (should be False): {empty_output}')
