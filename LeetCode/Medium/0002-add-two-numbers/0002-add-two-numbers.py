# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carried = 0
        while l1 and l2:
            s = l1.val + l2.val + carried
            if s >= 10:
                carried, s = 1, s - 10
            else:
                carried = 0
            
            curr.next = ListNode(val=s)
            curr, l1, l2 = curr.next, l1.next, l2.next
        
        while l1:
            s = l1.val + carried
            if s >= 10:
                carried, s = 1, s - 10
            else:
                carried = 0

            curr.next = ListNode(val=s)
            curr, l1 = curr.next, l1.next

        while l2:
            s = l2.val + carried
            if s >= 10:
                carried, s = 1, s - 10
            else:
                carried = 0

            curr.next = ListNode(val=s)
            curr, l2 = curr.next, l2.next

        if carried == 1:
            curr.next = ListNode(val=1)
        
        return head.next