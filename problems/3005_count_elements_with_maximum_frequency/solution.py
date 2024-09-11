from collections import defaultdict


class Solution:

    @staticmethod
    def max_frequency_elements(nums: list[int]) -> int:
        nums_frequencies: dict[int, int] = defaultdict(int)

        for num in nums:
            nums_frequencies[num] += 1

        max_frequency: int = 0

        for frequency in nums_frequencies.values():
            max_frequency = max(max_frequency, frequency)

        answer: int = 0

        for num, frequency in nums_frequencies.items():
            if frequency == max_frequency:
                answer += frequency

        return answer


solution = Solution()
example_1 = solution.max_frequency_elements(nums=[1, 2, 2, 3, 1, 4])
example_2 = solution.max_frequency_elements(nums=[1, 2, 3, 4, 5])

print(f'Example 1 output (should be 4): {example_1}')
print(f'Example 2 output (should be 5): {example_2}')
