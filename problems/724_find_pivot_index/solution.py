class Solution:

    @staticmethod
    def pivot_index(nums: list[int]) -> int:
        total_sum: int = sum(nums)
        left_sum: int = 0

        for i, num in enumerate(nums):
            right_sum: int = total_sum - left_sum - num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1


solution = Solution()
example_1 = solution.pivot_index(nums=[1, 7, 3, 6, 5, 6])
example_2 = solution.pivot_index(nums=[1, 2, 3])
example_3 = solution.pivot_index(nums=[2, 1, -1])

print(f'Example 1 output (should be 3): {example_1}')
print(f'Example 2 output (should be -1): {example_2}')
print(f'Example 3 output (should be 0): {example_3}')
