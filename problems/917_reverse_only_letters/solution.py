class Solution:

    @staticmethod
    def reverse_only_letters(s: str) -> str:
        s_chars: list[str] = list(s)
        left_index: int = 0
        right_index: int = len(s) - 1

        while left_index < right_index:
            if not s_chars[left_index].isalpha():
                left_index += 1
            elif not s_chars[right_index].isalpha():
                right_index -= 1
            else:
                s_chars[left_index], s_chars[right_index] = (
                    s_chars[right_index], s_chars[left_index]
                )
                left_index += 1
                right_index -= 1

        return ''.join(s_chars)


solution = Solution()
example_1 = solution.reverse_only_letters(s='ab-cd')
example_2 = solution.reverse_only_letters(s='a-bC-dEf-ghIj')
example_3 = solution.reverse_only_letters(s='Test1ng-Leet=code-Q!')

print(f'Example 1 output (should be "dc-ba"): {example_1}')
print(f'Example 2 output (should be "j-Ih-gfE-dCba"): {example_2}')
print(f'Example 3 output (should be "Qedo1ct-eeLg=ntse-T!"): {example_3}')
