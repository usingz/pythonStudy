from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self._next = next


def reversed_node(head: Node) -> Optional[Node]:
    reversed_head = None
    current = head
    while current:
        reversed_head, reversed_head._next, current = current, reversed_head, current._next
    return reversed_head


def check_circle(head: Node) -> bool:
    if not head:
        return False
    slow, fast = head, head
    while fast._next and fast:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False




