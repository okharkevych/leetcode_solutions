class Solution:

    @staticmethod
    def word_pattern(pattern: str, s: str) -> bool:
        words: list[str] = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word: dict[str, str] = {}
        word_to_char: dict[str, str] = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True


solution = Solution()
example_1 = solution.word_pattern(pattern='abba', s='dog cat cat dog')
example_2 = solution.word_pattern(pattern='abba', s='dog cat cat fish')
example_3 = solution.word_pattern(pattern='aaaa', s='dog cat cat dog')

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
print(f'Example 3 output (should be False): {example_3}')
