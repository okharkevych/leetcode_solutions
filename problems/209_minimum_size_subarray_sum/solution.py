class Solution:

    @staticmethod
    def min_sub_array_len(target: int, nums: list[int]) -> int:
        min_length: int | float = float('inf')
        current_sum: int = 0
        left_index: int = 0

        for right_index in range(len(nums)):
            current_sum += nums[right_index]

            while current_sum >= target:
                min_length = min(min_length, right_index - left_index + 1)
                current_sum -= nums[left_index]
                left_index += 1

        return min_length if min_length != float('inf') else 0


solution = Solution()
example_1 = solution.min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3])
example_2 = solution.min_sub_array_len(target=4, nums=[1, 4, 4])
example_3 = solution.min_sub_array_len(
    target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]
)

print(f'Example 1 output (should be 2): {example_1}')
print(f'Example 2 output (should be 1): {example_2}')
print(f'Example 3 output (should be 0): {example_3}')
