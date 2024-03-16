from math import inf
from typing import Optional, List

from exercises.leetcode._list_node import ListNode


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        lists = list(filter(lambda l: l, lists))

        i = 0
        res = None
        while i < len(lists):
            list1 = res
            list2 = lists[i]
            cur = dummy = ListNode()
            at = False
            while list1 and list2:
                at = True
                v1 = list1.val if list1 else +inf
                v2 = list2.val if list2 else +inf

                if v1 < v2:
                    cur.val = v1
                    list1 = list1.next if list1 else None
                else:
                    cur.val = v2
                    list2 = list2.next if list2 else None

                if list1 and list2:
                    cur.next = ListNode()
                    cur = cur.next

            if list1 or list2:
                if at:
                    cur.next = list1 if list1 else list2
                else:
                    dummy = list1 or list2

            res = dummy
            i += 1

        return res

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        lists = list(filter(lambda l: l, lists))

        i = 0
        res = None
        while i < len(lists):
            list1 = res
            list2 = lists[i]
            dummy = cur = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1, cur = list1.next, list1
                else:
                    cur.next = list2
                    list2, cur = list2.next, list2

            if list1 or list2:
                cur.next = list1 if list1 else list2

            res = dummy.next
            i += 1

        return res
