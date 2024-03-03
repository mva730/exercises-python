from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    flag = True
    base = ListNode()
    remainder = 0

    r = prev = base

    while flag:
        s = remainder
        if l1 and l2:
            s += l1.val + l2.val
        elif l1 and not l2:
            s += l1.val
        elif not l1 and l2:
            s += l2.val

        if s < 10:
            r.val = s
            remainder = 0
        else:
            r.val = s % 10
            remainder = 1

        r.next = ListNode()
        if l1 and l2:
            l1 = l1.next
            l2 = l2.next
        elif l1 and not l2:
            l1 = l1.next
            l2 = None
        elif not l1 and l2:
            l2 = l2.next
            l1 = None
        else:
            if remainder > 0:
                r.val = remainder
            else:
                if not r.val:
                    prev.next = None
                r.next = None

            flag = False
        prev = r
        r = r.next

    return base


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


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
node_list1 = makeNodeList(l1)
node_list2 = makeNodeList(l2)
print_list(node_list1)
print_list(node_list2)

print_list(addTwoNumbers(node_list1, node_list2))
