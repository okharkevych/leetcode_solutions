from collections import defaultdict


class Solution:

    def sum_of_unique(self, nums: list[int]) -> int:
        nums_count: dict[int, int] = defaultdict(int)

        for num in nums:
            nums_count[num] += 1

        answer: int = 0

        for num, count in nums_count.items():
            if count == 1:
                answer += num

        return answer


solution = Solution()
example_1 = solution.sum_of_unique(nums=[1, 2, 3, 2])
example_2 = solution.sum_of_unique(nums=[1, 1, 1, 1, 1])
example_3 = solution.sum_of_unique(nums=[1, 2, 3, 4, 5])

print(f'Example 1 output (should be 4): {example_1}')
print(f'Example 2 output (should be 0): {example_2}')
print(f'Example 3 output (should be 15): {example_3}')
