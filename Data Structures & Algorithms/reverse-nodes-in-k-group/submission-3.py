# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, head

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
            return tail

        while True:
            node = first
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            second = node.next
            first = reverseInBetween(first, second)

        return dummy.next