class Solution:

    @staticmethod
    def reverse_prefix(word: str, ch: str) -> str:
        ch_index: int = word.find(ch)

        if ch_index == -1:
            return word

        word_chars: list[str] = list(word)
        left_index: int = 0
        right_index: int = ch_index

        while left_index < right_index:
            word_chars[left_index], word_chars[right_index] = (
                word_chars[right_index], word_chars[left_index]
            )
            left_index += 1
            right_index -= 1

        return ''.join(word_chars)


solution = Solution()
example_1 = solution.reverse_prefix(word='abcdefd', ch='d')
example_2 = solution.reverse_prefix(word='xyxzxe', ch='z')
example_3 = solution.reverse_prefix(word='abcd', ch='z')

print(f'Example 1 output (should be "dcbaefd"): {example_1}')
print(f'Example 2 output (should be "zxyxxe"): {example_2}')
print(f'Example 3 output (should be "abcd"): {example_3}')
