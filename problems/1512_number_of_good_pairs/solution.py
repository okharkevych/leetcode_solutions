from collections import defaultdict


class Solution:

    @staticmethod
    def num_identical_pairs(nums: list[int]) -> int:
        num_counts: dict[int, int] = defaultdict(int)
        good_pairs: int = 0

        for num in nums:
            good_pairs += num_counts[num]
            num_counts[num] += 1

        return good_pairs


solution = Solution()
example_1 = solution.num_identical_pairs(nums=[1, 2, 3, 1, 1, 3])
example_2 = solution.num_identical_pairs(nums=[1, 1, 1, 1])
example_3 = solution.num_identical_pairs(nums=[1, 2, 3])

print(f'Example 1 output (should be 4): {example_1}')
print(f'Example 2 output (should be 6): {example_2}')
print(f'Example 3 output (should be 0): {example_3}')
