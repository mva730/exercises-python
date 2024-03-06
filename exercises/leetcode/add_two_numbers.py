from typing import Optional

from exercises.leetcode._list_node import ListNode, makeNodeList, print_list


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


def addTwoNumbers2(l1, l2):
    base = ListNode()
    current = base
    while l1 or l2:
        v1 = l1 and l1.val or 0
        v2 = l2 and l2.val or 0

        l1 = l1 and l1.next
        l2 = l2 and l2.next

        sum_result = v1 + v2 + current.val
        if sum_result > 9:
            current.next = ListNode(1)
        elif l1 or l2:
            current.next = ListNode()

        current.val = sum_result % 10
        current = current.next

    return base


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
node_list1 = makeNodeList(l1)
node_list2 = makeNodeList(l2)
print_list(node_list1)
print_list(node_list2)

print_list(addTwoNumbers(node_list1, node_list2))
