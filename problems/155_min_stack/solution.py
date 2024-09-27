class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
get_min_ouput_1 = obj.get_min()
obj.pop()
top_ouput = obj.top()
get_min_ouput_2 = obj.get_min()

print(f'get_min output 1 (should be -3): {get_min_ouput_1}')
print(f'top output (should be 0): {top_ouput}')
print(f'get_min output 2 (should be -2): {get_min_ouput_2}')
