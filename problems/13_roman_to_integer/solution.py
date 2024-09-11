import re


class Solution:

    @staticmethod
    def identify_separate_nums(roman_num: str) -> list[str]:
        roman_num_pattern: str = r'CM|CD|XC|XL|IX|IV|M|D|C|L|X|V|I'
        separate_nums = re.findall(
            pattern=roman_num_pattern, string=roman_num
        )

        return separate_nums

    def roman_to_int(self, s: str) -> int:
        roman_num_values: dict[str, int] = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }

        separate_roman_nums = self.identify_separate_nums(roman_num=s)
        separate_arabic_nums: list[int] = [
            roman_num_values[num] for num in separate_roman_nums
        ]

        conversion_result: int = sum(separate_arabic_nums)

        return conversion_result


solution = Solution()
example_1 = solution.roman_to_int(s='III')
example_2 = solution.roman_to_int(s='LVIII')
example_3 = solution.roman_to_int(s='MCMXCIV')

print(f'Example 1 output (should be 3): {example_1}')
print(f'Example 2 output (should be 58): {example_2}')
print(f'Example 3 output (should be 1994): {example_3}')
