# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, head
        reached = False

        for _ in range(k):
            second = second.next

        def reverseInBetween(begin: ListNode, end: ListNode):
            prev = None
            cur = begin.next
            tail = cur

            while cur != end:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            begin.next = prev
            tail.next = end

        while not reached:
            reverseInBetween(first, second)
            for _ in range(k):
                if not second:
                    return dummy.next
                first, second = first.next, second.next

        return dummy.next