class Solution:

    @staticmethod
    def is_valid(s: str) -> bool:
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()
example_1 = solution.is_valid(s='()')
example_2 = solution.is_valid(s='()[]{}')
example_3 = solution.is_valid(s='(]')

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be True): {example_2}')
print(f'Example 3 output (should be False): {example_3}')
