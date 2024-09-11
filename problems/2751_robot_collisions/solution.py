class Solution:

    @staticmethod
    def survived_robots_healths(
        positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        robots = sorted(
            zip(positions, healths, directions), key=lambda x: x[0]
        )
        stack = []

        for position, health, direction in robots:
            if direction == 'R':
                stack.append((position, health, direction))
            else:
                while stack and stack[-1][2] == 'R':
                    (
                        previous_position,
                        previous_health,
                        previous_direction
                    ) = stack[-1]
                    if previous_health > health:
                        stack[-1] = (
                            previous_position,
                            previous_health - 1,
                            previous_direction
                        )
                        break
                    elif previous_health < health:
                        stack.pop()
                        health -= 1
                    else:
                        stack.pop()
                        break
                else:
                    stack.append((position, health, direction))

        final_healths = {}
        for pos, health, _ in stack:
            final_healths[pos] = health

        return [
            final_healths[pos] for pos in positions if pos in final_healths
        ]


solution = Solution()
example_1 = solution.survived_robots_healths(
    positions=[5, 4, 3, 2, 1],
    healths=[2, 17, 9, 15, 10],
    directions='RRRRR'
)
example_2 = solution.survived_robots_healths(
    positions=[3, 5, 2, 6],
    healths=[10, 10, 15, 12],
    directions='RLRL'
)
example_3 = solution.survived_robots_healths(
    positions=[1, 2, 5, 6],
    healths=[10, 10, 11, 11],
    directions='RLRL'
)

print(f'Example 1 output (should be [2, 17, 9, 15, 10]): {example_1}')
print(f'Example 2 output (should be [14]): {example_2}')
print(f'Example 3 output (should be []): {example_3}')
