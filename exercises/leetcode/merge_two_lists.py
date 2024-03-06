from math import inf
from typing import Optional

from exercises.leetcode._list_node import ListNode


def mergeTwoLists(a, b):
    i = 0
    j = 0

    r = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1

    while i < len(a):
        r.append(a[i])
        i += 1

    while j < len(a):
        r.append(b[j])
        j += 1

    return r


print(mergeTwoLists([1, 2, 4], [1, 3, 4]))


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        a = ListNode()
        r = a
        while list1 and list2:
            if list1.val < list2.val:
                r.val = list1.val
                list1 = list1.next
            else:
                r.val = list2.val
                list2 = list2.next

            if list1 or list2:
                r.next = ListNode()
                r = r.next

        while list1:
            r.val = list1.val
            list1 = list1.next
            if list1:
                r.next = ListNode()
                r = r.next

        while list2:
            r.val = list2.val
            list2 = list2.next
            if list2:
                r.next = ListNode()
                r = r.next

        return a

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        dummy = cur = ListNode()
        while list1 or list2:
            v1 = list1.val if list1 else +inf
            v2 = list2.val if list2 else +inf

            if v1 < v2:
                cur.val = v1
                list1 = list1.next if list1 else None
            else:
                cur.val = v2
                list2 = list2.next if list2 else None

            if list1 or list2:
                cur.next = ListNode()
                cur = cur.next

        return dummy

