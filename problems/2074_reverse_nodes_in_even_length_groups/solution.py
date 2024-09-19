class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def reverse_even_length_groups(
        head: ListNode | None
    ) -> ListNode | None:
        if not head:
            return None

        def reverse_list(start, end):
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev, start

        current = head
        group_size = 1
        prev_group_tail = None

        while current:
            group_head = current
            count = 0

            while current and count < group_size:
                count += 1
                current = current.next

            if count % 2 == 0:
                new_group_head, new_group_tail = reverse_list(
                    group_head, current
                )
                if prev_group_tail:
                    prev_group_tail.next = new_group_head
                else:
                    head = new_group_head

                new_group_tail.next = current
                prev_group_tail = new_group_tail
            else:
                prev_group_tail = group_head
                for _ in range(count - 1):
                    prev_group_tail = prev_group_tail.next

            group_size += 1

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

head_1 = solution.create_linked_list(elements=[5, 2, 6, 3, 9, 1, 7, 3, 8, 4])
updated_linked_list_1 = solution.reverse_even_length_groups(head=head_1)
result_1 = solution.linked_list_to_list(head=updated_linked_list_1)
print(f'Example 1 output (should be [5,6,2,3,9,1,4,8,3,7]): {result_1}')

head_2 = solution.create_linked_list(elements=[1, 1, 0, 6])
updated_linked_list_2 = solution.reverse_even_length_groups(head=head_2)
result_2 = solution.linked_list_to_list(head=updated_linked_list_2)
print(f'\nExample 2 output (should be [1,0,1,6]): {result_2}')

head_3 = solution.create_linked_list(elements=[1, 1, 0, 6, 5])
updated_linked_list_3 = solution.reverse_even_length_groups(head=head_3)
result_3 = solution.linked_list_to_list(head=updated_linked_list_3)
print(f'\nExample 3 output (should be [1,0,1,5,6]): {result_3}')
