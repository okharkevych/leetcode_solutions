from collections import defaultdict


class Solution:

    @staticmethod
    def frequency_sort(s: str) -> str:
        char_count: dict[str, int] = defaultdict(int)

        for char in s:
            char_count[char] += 1

        sorted_chars: list[str] = sorted(
            char_count.keys(), key=lambda x: char_count[x], reverse=True
        )
        result: list[str] = []

        for char in sorted_chars:
            result.append(char * char_count[char])

        return ''.join(result)


solution = Solution()
example_1 = solution.frequency_sort(s='tree')
example_2 = solution.frequency_sort(s='cccaaa')
example_3 = solution.frequency_sort(s='Aabb')

print(f'Example 1 output (should be "eert" or "eetr"): {example_1}')
print(f'Example 2 output (should be "aaaccc" or "cccaaa"): {example_2}')
print(f'Example 3 output (should be "bbAa" or "bbaA"): {example_3}')
