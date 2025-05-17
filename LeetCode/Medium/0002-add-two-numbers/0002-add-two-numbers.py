# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carried = 0
        while l1 or l2 or carried:
            s = carried
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            if s >= 10:
                carried, s = 1, s - 10
            else:
                carried = 0
            
            curr.next = ListNode(val=s)
            curr = curr.next
        
        return head.next