# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        tmp = None
        curr = head
        while curr:
            nn = ListNode(curr.val, tmp)
            tmp = nn
            curr = curr.next
        return tmp