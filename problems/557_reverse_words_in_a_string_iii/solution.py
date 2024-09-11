class Solution:

    @staticmethod
    def reverse_word(word: str) -> str:
        left_index: int = 0
        right_index: int = len(word) - 1
        word_chars: list[str] = list(word)

        while left_index < right_index:
            word_chars[left_index], word_chars[right_index] = (
                word_chars[right_index], word_chars[left_index]
            )
            left_index += 1
            right_index -= 1

        return ''.join(word_chars)

    def reverse_words(self, s: str) -> str:
        words: list[str] = s.split()
        reversed_words = [self.reverse_word(word) for word in words]

        return ' '.join(reversed_words)


solution = Solution()
example_1 = solution.reverse_words(s='Let\'s take LeetCode contest')
example_2 = solution.reverse_words(s='Mr Ding')

print(
    f'Example 1 output (should be "s\'teL ekat edoCteeL tsetnoc"): {example_1}'
)
print(f'Example 2 output (should be "rM gniD"): {example_2}')
