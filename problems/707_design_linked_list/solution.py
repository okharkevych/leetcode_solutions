class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def add_at_head(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at_tail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def add_at_index(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.add_at_head(val)
            return

        new_node = ListNode(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1


linked_list = MyLinkedList()
add_at_head = linked_list.add_at_head(val=1)
add_at_tail = linked_list.add_at_tail(val=3)
add_at_index = linked_list.add_at_index(index=1, val=2)
get_1 = linked_list.get(index=1)
delete_at_index = linked_list.delete_at_index(index=1)
get_2 = linked_list.get(index=1)

print(f'get_1 output (should be 2): {get_1}')
print(f'get_2 output (should be 3): {get_2}')
