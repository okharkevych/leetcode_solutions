from collections import Counter


class Solution:

    @staticmethod
    def check_inclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count: dict[str, int] = Counter(s1)
        s2_count: dict[str, int] = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            start_char: str = s2[i - len(s1)]
            new_char: str = s2[i]

            s2_count[new_char] += 1
            s2_count[start_char] -= 1

            if s2_count[start_char] == 0:
                del s2_count[start_char]

            if s1_count == s2_count:
                return True

        return False


solution = Solution()
example_1 = solution.check_inclusion(s1='ab', s2='eidbaooo')
example_2 = solution.check_inclusion(s1='ab', s2='eidboaoo')

print(f'Example 1 output (should be True): {example_1}')
print(f'Example 2 output (should be False): {example_2}')
