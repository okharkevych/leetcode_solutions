class Solution:

    @staticmethod
    def close_strings(word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1: dict[str, int] = {}
        freq2: dict[str, int] = {}

        unique1: set[str] = set(word1)
        unique2: set[str] = set(word2)

        if unique1 != unique2:
            return False

        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1

        return sorted(freq1.values()) == sorted(freq2.values())


solution = Solution()
example_1 = solution.close_strings(word1='abc', word2='bca')
example_2 = solution.close_strings(word1='a', word2='aa')
example_3 = solution.close_strings(word1='cabbba', word2='abbccc')

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
print(f'Example 3 output (should be True): {example_3}')
