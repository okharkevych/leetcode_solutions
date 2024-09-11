from collections import defaultdict


class Solution:

    @staticmethod
    def max_subarray_length(nums: list[int], k: int) -> int:
        left_index: int = 0
        max_length: int = 0
        exceed_count: int = 0
        num_counts: dict[int, int] = defaultdict(int)

        for right_index in range(len(nums)):
            num_counts[nums[right_index]] += 1

            if num_counts[nums[right_index]] > k:
                exceed_count += 1

            while exceed_count > 0:
                if num_counts[nums[left_index]] > k:
                    exceed_count -= 1

                num_counts[nums[left_index]] -= 1

                if num_counts[nums[left_index]] == 0:
                    del num_counts[nums[left_index]]

                left_index += 1

            max_length = max(max_length, right_index - left_index + 1)

        return max_length


solution = Solution()
example_1 = solution.max_subarray_length(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2)
example_2 = solution.max_subarray_length(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1)
example_3 = solution.max_subarray_length(nums=[5, 5, 5, 5, 5, 5, 5], k=4)

print(f'Example 1 output (should be 6): {example_1}')
print(f'Example 2 output (should be 2): {example_2}')
print(f'Example 3 output (should be 4): {example_3}')
