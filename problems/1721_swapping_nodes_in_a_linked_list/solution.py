class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def swap_nodes(head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return None

        first = last = head
        for _ in range(k - 1):
            first = first.next

        temp = first
        while temp.next:
            temp = temp.next
            last = last.next

        first.val, last.val = last.val, first.val

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

head_1 = solution.create_linked_list(elements=[1, 2, 3, 4, 5])
updated_linked_list_1 = solution.swap_nodes(head=head_1, k=2)
result_1 = solution.linked_list_to_list(head=updated_linked_list_1)
print(f'Example 1 output (should be [1,4,3,2,5]): {result_1}')

head_2 = solution.create_linked_list(elements=[7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
updated_linked_list_2 = solution.swap_nodes(head=head_2, k=5)
result_2 = solution.linked_list_to_list(head=updated_linked_list_2)
print(f'\nExample 2 output (should be [7,9,6,6,8,7,3,0,9,5]): {result_2}')
