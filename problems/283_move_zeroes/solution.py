class Solution:

    @staticmethod
    def move_zeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_index: int = 0

        for right_index in range(len(nums)):
            if nums[right_index] != 0:
                nums[left_index], nums[right_index] = (
                    nums[right_index], nums[left_index]
                )
                left_index += 1

        # return nums

# solution = Solution()
# example_1 = solution.move_zeroes(nums=[0, 1, 0, 3, 12])
# example_2 = solution.move_zeroes(nums=[0])
#
# print(f'Example 1 output (should be [1,3,12,0,0]): {example_1}')
# print(f'Example 2 output (should be [0]): {example_2}')
