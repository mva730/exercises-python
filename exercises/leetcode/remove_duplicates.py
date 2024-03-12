from typing import Optional

from exercises.leetcode._list_node import ListNode, makeNodeList, print_list


class Solution:
    def deleteDuplicatesSorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = set()
        prev = current = head

        while current:
            if current.val in temp:
                if current.next:
                    prev.next = current.next
                else:
                    prev.next = None
                current = prev.next
                continue

            temp.add(current.val)
            prev = current
            current = current.next

        return head


print_list(Solution().deleteDuplicates(makeNodeList([2, 3, 1, 1, 1, 2])))
print_list(Solution().deleteDuplicatesSorted(makeNodeList([1, 1, 1, 2, 2])))
