class Solution:

    def custom_sort_string(self, order: str, s: str) -> str:
        order_map: dict[str, int] = {
            char: position for position, char in enumerate(order)
        }

        sorted_s: list[str] = sorted(
            s, key=lambda char: order_map.get(char, len(order))
        )

        return ''.join(sorted_s)


solution = Solution()
example_1 = solution.custom_sort_string(order='cba', s='abcd')
example_2 = solution.custom_sort_string(order='bcafg', s='abcd')

print(f'Example 1 output (should be "cbad"): {example_1}')
print(f'Example 2 output (should be "bcad"): {example_2}')
