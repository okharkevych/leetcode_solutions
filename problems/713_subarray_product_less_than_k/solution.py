class Solution:

    @staticmethod
    def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left_index: int = 0
        product: int = 1
        answer: int = 0

        for right_index in range(len(nums)):
            product *= nums[right_index]

            while product >= k:
                product /= nums[left_index]
                left_index += 1

            answer += right_index - left_index + 1

        return answer


solution = Solution()
example_1 = solution.num_subarray_product_less_than_k(
    nums=[10, 5, 2, 6], k=100
)
example_2 = solution.num_subarray_product_less_than_k(nums=[1, 2, 3], k=0)

print(f'Example 1 output (should be 8): {example_1}')
print(f'Example 2 output (should be 0): {example_2}')
