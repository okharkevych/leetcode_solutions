class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

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

head_1 = solution.create_linked_list(elements=[1, 2, 6, 3, 4, 5, 6])
updated_linked_list_1 = solution.remove_elements(head=head_1, val=6)
result_1 = solution.linked_list_to_list(head=updated_linked_list_1)
print(f'Example 1 output (should be [1,2,3,4,5]): {result_1}')

head_2 = solution.create_linked_list(elements=[])
updated_linked_list_2 = solution.remove_elements(head=head_2, val=1)
result_2 = solution.linked_list_to_list(head=updated_linked_list_2)
print(f'\nExample 2 output (should be []): {result_2}')

head_3 = solution.create_linked_list(elements=[7, 7, 7, 7])
updated_linked_list_3 = solution.remove_elements(head=head_3, val=7)
result_3 = solution.linked_list_to_list(head=updated_linked_list_3)
print(f'\nExample 3 output (should be []): {result_3}')
