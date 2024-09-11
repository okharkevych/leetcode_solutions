from collections import defaultdict


class Solution:

    @staticmethod
    def unique_occurrences(arr: list[int]) -> bool:
        num_occurrences: dict[int, int] = defaultdict(int)

        for num in arr:
            num_occurrences[num] += 1

        unique_occurrences: set[int] = set(num_occurrences.values())

        return len(unique_occurrences) == len(num_occurrences)


solution = Solution()
example_1 = solution.unique_occurrences(arr=[1, 2, 2, 1, 1, 3])
example_2 = solution.unique_occurrences(arr=[1, 2])
example_3 = solution.unique_occurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
print(f'Example 3 output (should be True): {example_3}')
