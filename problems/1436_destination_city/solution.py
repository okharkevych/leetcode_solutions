class Solution:

    @staticmethod
    def dest_city(paths: list[list[str]]) -> str:
        outgoing: set[str] = set()

        for path in paths:
            outgoing.add(path[0])

        for path in paths:
            if path[1] not in outgoing:
                return path[1]


solution = Solution()
example_1 = solution.dest_city(
    paths=[
        ["London", "New York"],
        ["New York", "Lima"],
        ["Lima", "Sao Paulo"]
    ]
)
example_2 = solution.dest_city(paths=[["B", "C"], ["D", "B"], ["C", "A"]])
example_3 = solution.dest_city(paths=[["A", "Z"]])

print(f'Example 1 output (should be "Sao Paulo"): {example_1}')
print(f'Example 2 output (should be "A"): {example_2}')
print(f'Example 3 output (should be "Z"): {example_3}')
