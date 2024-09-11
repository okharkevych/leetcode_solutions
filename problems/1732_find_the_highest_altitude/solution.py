class Solution:

    @staticmethod
    def largest_altitude(gain: list[int]) -> int:
        prefix: list[int] = [0]

        for i in range(len(gain)):
            prefix.append(gain[i] + prefix[-1])

        return max(prefix)


solution = Solution()
example_1 = solution.largest_altitude(gain=[-5, 1, 5, 0, -7])
example_2 = solution.largest_altitude(gain=[-4, -3, -2, -1, 4, 3, 2])

print(f'Example 1 output (should be 1): {example_1}')
print(f'Example 2 output (should be 0): {example_2}')
