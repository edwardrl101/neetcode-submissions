# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        def reverse(node):
            prev, curr = None, node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        l2 = reverse(slow.next)
        slow.next = None
        l1 = head
        while l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2
