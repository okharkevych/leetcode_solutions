class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def delete_middle(head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None

        slow_pointer = head
        fast_pointer = head
        prev = None

        while fast_pointer and fast_pointer.next:
            prev = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        prev.next = slow_pointer.next

        return head

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

head_1 = solution.create_linked_list(elements=[1, 3, 4, 7, 1, 2, 6])
updated_linked_list_1 = solution.delete_middle(head=head_1)
result_1 = solution.linked_list_to_list(head=updated_linked_list_1)
print(f'Example 1 output (should be [1,3,4,1,2,6]): {result_1}')

head_2 = solution.create_linked_list(elements=[1, 2, 3, 4])
updated_linked_list_2 = solution.delete_middle(head=head_2)
result_2 = solution.linked_list_to_list(head=updated_linked_list_2)
print(f'\nExample 2 output (should be [1,2,4]): {result_2}')

head_3 = solution.create_linked_list(elements=[2, 1])
updated_linked_list_3 = solution.delete_middle(head=head_3)
result_3 = solution.linked_list_to_list(head=updated_linked_list_3)
print(f'\nExample 3 output (should be [2]): {result_3}')
