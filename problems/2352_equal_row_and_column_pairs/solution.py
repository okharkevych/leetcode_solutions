from collections import defaultdict


class Solution:

    @staticmethod
    def equal_pairs(grid: list[list[int]]) -> int:
        n = len(grid)
        row_hashes = defaultdict(int)

        for row in grid:
            row_hashes[tuple(row)] += 1

        equal_pairs_count = 0

        for col in range(n):
            col_hash = tuple(grid[row][col] for row in range(n))
            if col_hash in row_hashes:
                equal_pairs_count += row_hashes[col_hash]

        return equal_pairs_count


solution = Solution()
example_1 = solution.equal_pairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]])
example_2 = solution.equal_pairs(
    grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
)

print(f'Example 1 output (should be 1): {example_1}')
print(f'Example 2 output (should be 3): {example_2}')
