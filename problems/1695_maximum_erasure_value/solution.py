class Solution:

    @staticmethod
    def maximum_unique_subarray(nums: list[int]) -> int:
        num_set: set[int] = set()
        left_index: int = 0
        current_sum: int = 0
        max_sum: int = 0

        for right_index in range(len(nums)):
            while nums[right_index] in num_set:
                num_set.remove(nums[left_index])
                current_sum -= nums[left_index]
                left_index += 1

            num_set.add(nums[right_index])
            current_sum += nums[right_index]
            max_sum = max(max_sum, current_sum)

        return max_sum


solution = Solution()
example_1 = solution.maximum_unique_subarray(nums=[4, 2, 4, 5, 6])
example_2 = solution.maximum_unique_subarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5])

print(f'Example 1 output (should be 17): {example_1}')
print(f'Example 2 output (should be 8): {example_2}')
