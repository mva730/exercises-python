from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makeNodeList(arr) -> Optional[ListNode]:
    base = ListNode()
    r = base
    for i in range(len(arr)):
        r.val = arr[i]
        if i + 1 < len(arr):
            r.next = ListNode()
            r = r.next
        else:
            r.next = None

    return base


def print_list(l):
    while l:
        print(l.val, end=' ')
        l = l.next
    print()
