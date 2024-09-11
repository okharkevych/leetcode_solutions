class Solution:

    @staticmethod
    def get_common(nums1: list[int], nums2: list[int]) -> int:
        pointer_1: int = 0
        pointer_2: int = 0

        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] == nums2[pointer_2]:
                return nums1[pointer_1]
            elif nums1[pointer_1] < nums2[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 += 1

        return -1


solution = Solution()
example_1 = solution.get_common(nums1=[1, 2, 3], nums2=[2, 4])
example_2 = solution.get_common(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5])

print(f'Example 1 output (should be 2): {example_1}')
print(f'Example 2 output (should be 2): {example_2}')
