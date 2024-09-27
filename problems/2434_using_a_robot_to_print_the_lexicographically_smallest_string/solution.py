class Solution:

    @staticmethod
    def robot_with_string(s: str) -> str:
        stack = []
        result = []

        min_right = [None] * len(s)
        min_right[-1] = s[-1]
        for i in range(len(s) - 2, -1, -1):
            min_right[i] = min(s[i], min_right[i + 1])

        for i, char in enumerate(s):
            stack.append(char)

            while stack and stack[-1] <= (
                min_right[i + 1 if i + 1 < len(s) else i]
            ):
                result.append(stack.pop())

        while stack:
            result.append(stack.pop())

        return ''.join(result)


solution = Solution()
example_1 = solution.robot_with_string(s='zza')
example_2 = solution.robot_with_string(s='bac')
example_3 = solution.robot_with_string(s='bdda')

print(f'Example 1 output (should be "azz"): {example_1}')
print(f'Example 2 output (should be "abc"): {example_2}')
print(f'Example 3 output (should be "addb"): {example_3}')
