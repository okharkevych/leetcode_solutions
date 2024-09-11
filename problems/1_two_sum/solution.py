class Solution:

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                indices: list[int] = [i, j]
                sum_of_pair: int = nums[i] + nums[j]

                if sum_of_pair == target:
                    return indices


solution = Solution()
example_1 = solution.two_sum(nums=[2, 7, 11, 15], target=9)
example_2 = solution.two_sum(nums=[3, 2, 4], target=6)
example_3 = solution.two_sum(nums=[3, 3], target=6)

print(f'Example 1 output (should be [0,1]): {example_1}')
print(f'Example 2 output (should be [1,2]): {example_2}')
print(f'Example 3 output (should be [0,1]): {example_3}')
