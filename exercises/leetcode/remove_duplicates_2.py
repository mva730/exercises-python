from typing import Optional

from exercises.leetcode._list_node import ListNode, makeNodeList


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = set()
        repeated = set()
        prev = current = head
        while current:
            if current.val in temp:
                repeated.add(current.val)
                if current.next:
                    prev.next = current.next
                else:
                    prev.next = None
                current = prev.next
                continue
            else:
                temp.add(current.val)

            prev = current
            current = current.next

        return self.makeNodeList(list(temp.difference(repeated)))

    def makeNodeList(self, arr) -> Optional[ListNode]:
        arr.sort()
        if not arr:
            return None
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


print(Solution().deleteDuplicates(makeNodeList([2, 3, 1, 1, 1, 2])))
