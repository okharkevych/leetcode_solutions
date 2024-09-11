class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def pair_sum(head: ListNode | None) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        max_twin_sum = 0
        left, right = head, prev
        while right:
            twin_sum = left.val + right.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            left = left.next
            right = right.next

        return max_twin_sum

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

head_1 = solution.create_linked_list(elements=[5, 4, 2, 1])
twin_sum_1 = solution.pair_sum(head=head_1)
print(f'Example 1 output (should be 6): {twin_sum_1}')

head_2 = solution.create_linked_list(elements=[4, 2, 2, 3])
twin_sum_2 = solution.pair_sum(head=head_2)
print(f'\nExample 2 output (should be 7): {twin_sum_2}')

head_3 = solution.create_linked_list(elements=[1, 100000])
twin_sum_3 = solution.pair_sum(head=head_3)
print(f'\nExample 2 output (should be 100001): {twin_sum_3}')
