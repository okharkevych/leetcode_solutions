class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


solution = NumArray(nums=[-2, 0, 3, -5, 2, -1])
example_1 = solution.sum_range(left=0, right=2)
example_2 = solution.sum_range(left=2, right=5)
example_3 = solution.sum_range(left=0, right=5)

print(f'Example 1 output (should be 1): {example_1}')
print(f'Example 1 output (should be -1): {example_2}')
print(f'Example 1 output (should be -3): {example_3}')
