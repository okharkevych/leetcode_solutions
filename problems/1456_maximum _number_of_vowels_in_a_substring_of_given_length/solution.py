class Solution:

    @staticmethod
    def max_vowels(s: str, k: int) -> int:
        vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
        current_vowels: int = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels: int = current_vowels

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels


solution = Solution()
example_1 = solution.max_vowels(s='abciiidef', k=3)
example_2 = solution.max_vowels(s='aeiou', k=2)
example_3 = solution.max_vowels(s='leetcode', k=3)

print(f'Example 1 output (should be 3): {example_1}')
print(f'Example 2 output (should be 2): {example_2}')
print(f'Example 3 output (should be 2: {example_3}')
