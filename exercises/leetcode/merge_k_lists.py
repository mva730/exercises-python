from math import inf
from typing import Optional, List

from exercises.leetcode._list_node import ListNode, makeNodeList, print_list


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        lists = list(filter(lambda l: l, lists))
        i = 0
        res = None
        while i < len(lists):
            list1 = res
            list2 = lists[i]
            if res is None:
                res = list2
                i += 1
                continue

            cur = dummy = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    cur.val = list1.val
                    list1 = list1.next
                else:
                    cur.val = list2.val
                    list2 = list2.next

                if list1 and list2:
                    cur.next = ListNode()
                    cur = cur.next

            if list1 or list2:
                cur.next = list1 if list1 else list2

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


l1 = makeNodeList([1, 4, 5])
l2 = makeNodeList([1, 3, 4])
l3 = makeNodeList([2, 6])

print_list(Solution().mergeKLists([l1, l2, l3]))
