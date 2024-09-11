class Solution:

    @staticmethod
    def heightchecker(heights: list[int]) -> int:
        expected: list[int] = sorted(heights)
        wrong_heights: list[int] = []
        i: int = 0

        while i < len(heights):
            if heights[i] != expected[i]:
                wrong_heights.append(i)
            i += 1

        return len(wrong_heights)


solution = Solution()
example_1 = solution.heightchecker(heights=[1, 1, 4, 2, 1, 3])
example_2 = solution.heightchecker(heights=[5, 1, 2, 3, 4])
example_3 = solution.heightchecker(heights=[1, 2, 3, 4, 5])

print(f'Example 1 output (should be 3): {example_1}')
print(f'Example 2 output (should be 5): {example_2}')
print(f'Example 3 output (should be 0): {example_3}')
