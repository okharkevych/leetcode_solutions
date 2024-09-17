class Solution:

    @staticmethod
    def remove_duplicates(nums: list[int]) -> int:
        if not nums:
            return 0

        slow_pointer = 0

        for fast_pointer in range(1, len(nums)):
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]

        return slow_pointer + 1

solution = Solution()
example_1 = solution.remove_duplicates(nums=[1,1,2])
example_2 = solution.remove_duplicates(nums=[0,0,1,1,1,2,2,3,3,4])

print(f'Example 1 output (should be 2): {example_1}')
print(f'Example 2 output (should be 5): {example_2}')
