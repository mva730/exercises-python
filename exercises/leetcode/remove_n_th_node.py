from typing import Optional

from exercises.leetcode._list_node import ListNode, makeNodeList, print_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        index = length - n

        prev = current = head
        i = 0
        while current:
            if i == index:
                if index == 0:
                    head = head.next
                    break

                if current.next:
                    prev.next = current.next
                else:
                    prev.next = None
                break
            prev = current
            current = current.next
            i += 1

        return head


print_list(Solution().removeNthFromEnd(makeNodeList([1, 2]), 2))
