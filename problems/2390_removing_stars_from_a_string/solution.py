class Solution:

    @staticmethod
    def remove_stars(s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


solution = Solution()
example_1 = solution.remove_stars(s='leet**cod*e')
example_2 = solution.remove_stars(s='erase*****')

print(f'Example 1 output (should be "lecoe"): {example_1}')
print(f'Example 2 output (should be ""): {example_2}')
