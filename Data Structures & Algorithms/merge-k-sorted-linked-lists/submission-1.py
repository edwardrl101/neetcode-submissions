# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1:
                return list2
            if not list2:
                return list1
            dummy = ListNode(0, list1) if list1.val < list2.val else ListNode(0, list2) 
            cur = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            
            res = list1 if list1 else list2
            cur.next = res

            return dummy.next

        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeTwoLists(res, lists[i])

        return res