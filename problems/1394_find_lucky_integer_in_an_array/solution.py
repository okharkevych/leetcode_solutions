from collections import defaultdict


class Solution:

    @staticmethod
    def find_lucky(arr: list[int]) -> int:
        num_count: dict[int, int] = defaultdict(int)

        for num in arr:
            num_count[num] += 1

        answer: int = -1

        for num, count in num_count.items():
            if num == count:
                answer = max(answer, num)

        return answer


solution = Solution()
example_1 = solution.find_lucky(arr=[2, 2, 3, 4])
example_2 = solution.find_lucky(arr=[1, 2, 2, 3, 3, 3])
example_3 = solution.find_lucky(arr=[2, 2, 2, 3, 3])

print(f'Example 1 output (should be 2): {example_1}')
print(f'Example 2 output (should be 3): {example_2}')
print(f'Example 3 output (should be -1): {example_3}')
