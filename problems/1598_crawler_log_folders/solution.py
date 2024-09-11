class Solution:

    @staticmethod
    def min_operations(logs: list[str]) -> int:
        move_back: str = '../'
        depth_counter: int = 0

        for log in logs:
            if not '.' in log:
                depth_counter += 1

            if log == move_back and depth_counter > 0:
                depth_counter -= 1

        return depth_counter


solution = Solution()
example_1 = solution.min_operations(logs=['d1/', 'd2/', '../', 'd21/', './'])
example_2 = solution.min_operations(
    logs=['d1/', 'd2/', './', 'd3/', '../', 'd31/']
)
example_3 = solution.min_operations(logs=['d1/', '../', '../', '../'])

print(f'Example 1 output (should be 2): {example_1}')
print(f'Example 2 output (should be 3): {example_2}')
print(f'Example 3 output (should be 0): {example_3}')
