class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def delete_duplicates(head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next

            head = head.next

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

head_1 = solution.create_linked_list(elements=[1, 2, 3, 3, 4, 4, 5])
updated_linked_list_1 = solution.delete_duplicates(head=head_1)
result_1 = solution.linked_list_to_list(head=updated_linked_list_1)
print(f'Example 1 output (should be [1,2,5]): {result_1}')

head_2 = solution.create_linked_list(elements=[1, 1, 1, 2, 3])
updated_linked_list_2 = solution.delete_duplicates(head=head_2)
result_2 = solution.linked_list_to_list(head=updated_linked_list_2)
print(f'\nExample 2 output (should be [2,3]): {result_2}')
