class Solution:

    @staticmethod
    def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
        total_drunk = num_bottles
        empty_bottles = num_bottles

        while empty_bottles >= num_exchange:
            new_bottles = empty_bottles // num_exchange
            total_drunk += new_bottles
            empty_bottles = empty_bottles % num_exchange + new_bottles

        return total_drunk


solution = Solution()
example_1 = solution.num_water_bottles(num_bottles=9, num_exchange=3)
example_2 = solution.num_water_bottles(num_bottles=15, num_exchange=4)

print(f'Example 1 output (should be 13): {example_1}')
print(f'Example 2 output (should be 19): {example_2}')
