class Solution:

    @staticmethod
    def equal_substring(s: str, t: str, max_cost: int) -> int:
        cost: list[int] = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        max_len: int = 0
        current_cost: int = 0
        left_index: int = 0

        for right_index in range(len(s)):
            current_cost += cost[right_index]

            while current_cost > max_cost:
                current_cost -= cost[left_index]
                left_index += 1

            max_len = max(max_len, right_index - left_index + 1)

        return max_len


solution = Solution()
example_1 = solution.equal_substring(s='abcd', t='bcdf', max_cost=3)
example_2 = solution.equal_substring(s='abcd', t='cdef', max_cost=3)
example_3 = solution.equal_substring(s='abcd', t='acde', max_cost=0)

print(f'Example 1 output (should be 3): {example_1}')
print(f'Example 2 output (should be 1): {example_2}')
print(f'Example 3 output (should be 1): {example_3}')
