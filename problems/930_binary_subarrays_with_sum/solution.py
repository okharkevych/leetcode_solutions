class Solution:

    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        prefix_sum_counts: dict[int, int] = {0: 1}
        current_sum: int = 0
        subarray_counts: int = 0

        for num in nums:
            current_sum += num
            target_sum = current_sum - goal

            if target_sum in prefix_sum_counts:
                subarray_counts += prefix_sum_counts[target_sum]

            if current_sum in prefix_sum_counts:
                prefix_sum_counts[current_sum] += 1
            else:
                prefix_sum_counts[current_sum] = 1

        return subarray_counts


solution = Solution()
example_1 = solution.num_subarrays_with_sum(nums=[1, 0, 1, 0, 1], goal=2)
example_2 = solution.num_subarrays_with_sum(nums=[0, 0, 0, 0, 0], goal=0)

print(f'Example 1 output (should be 4): {example_1}')
print(f'Example 2 output (should be 15): {example_2}')
