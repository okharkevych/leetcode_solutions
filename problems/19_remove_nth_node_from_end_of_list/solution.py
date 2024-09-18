class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def remove_nth_from_end(
        head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(0, head)
        slow_pointer = dummy
        fast_pointer = dummy

        for _ in range(n + 1):
            fast_pointer = fast_pointer.next

        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        slow_pointer.next = slow_pointer.next.next

        return dummy.next

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

    @staticmethod
    def linked_list_to_list(head: ListNode | None) -> list[int]:
        elements: list[int] = []

        while head:
            elements.append(head.val)
            head = head.next

        return elements


solution = Solution()

head_1 = solution.create_linked_list(elements=[1, 2, 3, 4, 5])
updated_linked_list_1 = solution.remove_nth_from_end(head=head_1, n=2)
result_1 = solution.linked_list_to_list(head=updated_linked_list_1)
print(f'Example 1 output (should be [1,2,3,5]): {result_1}')

head_2 = solution.create_linked_list(elements=[1])
updated_linked_list_2 = solution.remove_nth_from_end(head=head_2, n=1)
result_2 = solution.linked_list_to_list(head=updated_linked_list_2)
print(f'\nExample 2 output (should be []): {result_2}')

head_3 = solution.create_linked_list(elements=[1, 2])
updated_linked_list_3 = solution.remove_nth_from_end(head=head_3, n=1)
result_3 = solution.linked_list_to_list(head=updated_linked_list_3)
print(f'\nExample 3 output (should be [1]): {result_3}')
