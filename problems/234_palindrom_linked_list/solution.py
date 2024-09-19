class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def is_palindrome(head: ListNode | None) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

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

head_1 = solution.create_linked_list(elements=[1, 2, 2, 1])
result_1 = solution.is_palindrome(head=head_1)
print(f'Example 1 output (should be True): {result_1}')

head_2 = solution.create_linked_list(elements=[1, 2])
result_2 = solution.is_palindrome(head=head_2)
print(f'\nExample 2 output (should be False): {result_2}')
