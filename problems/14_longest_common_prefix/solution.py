class Solution:

    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]


solution = Solution()
example_1 = solution.longest_common_prefix(strs=['flower', 'flow', 'flight'])
example_2 = solution.longest_common_prefix(strs=['dog', 'racecar', 'car'])

print(f'Example 1 output (should be "fl"): {example_1}')
print(f'Example 2 output (should be ""): {example_2}')
