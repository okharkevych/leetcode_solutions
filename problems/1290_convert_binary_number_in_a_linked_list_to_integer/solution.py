class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def get_decimal_value(head: ListNode) -> int:
        num = 0
        current = head

        while current:
            num = (num << 1) | current.val
            current = current.next

        return num

    @staticmethod
    def create_linked_list(elements: list[int]) -> ListNode | None:
        if not elements:
            return None

        head = ListNode(elements[0])
        current = head

        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next

        return head


solution = Solution()

head_1 = solution.create_linked_list(elements=[1, 0, 1])
result_1 = solution.get_decimal_value(head=head_1)
print(f'Example 1 output (should be 5): {result_1}')

head_2 = solution.create_linked_list(elements=[0])
result_2 = solution.get_decimal_value(head=head_2)
print(f'\nExample 2 output (should be 0): {result_2}')
