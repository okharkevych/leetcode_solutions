class Solution:

    @staticmethod
    def find_the_winner(n: int, k: int) -> int:
        friends: list[int] = list(range(1, n + 1))
        index: int = 0

        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)

        return friends[0]


solution = Solution()
example_1 = solution.find_the_winner(n=5, k=2)
example_2 = solution.find_the_winner(n=6, k=5)

print(f'Example 1 output (should be 3): {example_1}')
print(f'Example 2 output (should be 1): {example_2}')
