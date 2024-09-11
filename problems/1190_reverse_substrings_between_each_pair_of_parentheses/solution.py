class Solution:

    @staticmethod
    def reverse_parentheses(s: str) -> str:
        stack: list[str] = []

        for char in s:
            if char == ')':
                temp: list[str] = []

                while stack and stack[-1] != '(':
                    temp.append(stack.pop())

                if stack and stack[-1] == '(':
                    stack.pop()

                stack.extend(temp)
            else:
                stack.append(char)

        return ''.join(stack)


solution = Solution()
example_1 = solution.reverse_parentheses(s='(abcd)')
example_2 = solution.reverse_parentheses(s='(u(love)i)')
example_3 = solution.reverse_parentheses(s='(ed(et(oc))el)')

print(f'Example 1 output (should be dcba): {example_1}')
print(f'Example 2 output (should be iloveu): {example_2}')
print(f'Example 3 output (should be leetcode): {example_3}')
