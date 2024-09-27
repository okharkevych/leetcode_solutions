class Solution:

    @staticmethod
    def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pop_index = 0

        for val in pushed:
            stack.append(val)

            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

        return not stack


solution = Solution()
example_1 = solution.validate_stack_sequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]
)
example_2 = solution.validate_stack_sequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]
)

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
