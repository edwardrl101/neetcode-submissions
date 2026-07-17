# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, head
        for _ in range(right):
            if _ < left-1:
                first = first.next
            second = second.next

        prev = None
        cur = first.next
        tail = cur

        while cur != second:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        first.next = prev
        tail.next = second

        return dummy.next