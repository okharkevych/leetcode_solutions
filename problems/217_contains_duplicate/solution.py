from collections import defaultdict


class Solution:

    @staticmethod
    def contains_duplicate(nums: list[int]) -> bool:
        num_counts: dict[int, int] = defaultdict(int)

        for num in nums:
            num_counts[num] += 1

        for num_count in tuple(num_counts.values()):
            if num_count > 1:
                return True

        return False


solution = Solution()
example_1 = solution.contains_duplicate(nums=[1, 2, 3, 1])
example_2 = solution.contains_duplicate(nums=[1, 2, 3, 4])
example_3 = solution.contains_duplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
print(f'Example 3 output (should be True): {example_3}')
