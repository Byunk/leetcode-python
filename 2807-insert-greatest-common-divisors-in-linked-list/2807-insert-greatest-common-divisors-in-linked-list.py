# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        l, r = head, head.next
        while r:
            divisor = self.getGreatestCommonDivisor(l.val, r.val)
            l.next = ListNode(val=divisor, next=r)
            l = l.next.next
            r = r.next

        return head

    def getGreatestCommonDivisor(self, l: int, r: int) -> int:
        for i in range(min(l, r)+1, 0, -1):
            if l % i == 0 and r % i == 0:
                return i

        raise NotImplementedError

