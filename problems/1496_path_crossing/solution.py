class Solution:

    def is_path_crossing(self, path: str) -> bool:
        visited: set[tuple[int, int]] = set()
        x: int = 0
        y: int = 0
        visited.add((x, y))

        direction_map: dict[str, tuple[int, int]] = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        for move in path:
            dx, dy = direction_map[move]
            x += dx
            y += dy

            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False


solution = Solution()
example_1 = solution.is_path_crossing(path='NES')
example_2 = solution.is_path_crossing(path='NESWW')

print(f'Example 1 output (should be False): {example_1}')
print(f'Example 2 output (should be True): {example_2}')
