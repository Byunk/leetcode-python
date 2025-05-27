# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        root = curr = ListNode(next=head)

        while curr and curr.next and curr.next.next:
            left, right = curr.next, curr.next.next
            curr.next, left.next, right.next = right, right.next, left
            curr = left
        
        return root.next