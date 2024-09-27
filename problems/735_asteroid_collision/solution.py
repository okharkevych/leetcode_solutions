class Solution:

    @staticmethod
    def asteroid_collision(asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


solution = Solution()
example_1 = solution.asteroid_collision(asteroids=[5, 10, -5])
example_2 = solution.asteroid_collision(asteroids=[8, -8])
example_3 = solution.asteroid_collision(asteroids=[10, 2, -5])

print(f'Example 1 output (should be [5,10]): {example_1}')
print(f'Example 2 output (should be []): {example_2}')
print(f'Example 3 output (should be [10]): {example_3}')
