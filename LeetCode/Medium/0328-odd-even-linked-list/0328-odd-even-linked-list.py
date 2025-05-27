# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd_root, even_root = ListNode(next=head), ListNode(next=head.next)
        left, right = odd_root.next, even_root.next

        while right and right.next:
            left.next, right.next = right.next, right.next.next
            left, right = left.next, right.next

        left.next = even_root.next
        return odd_root.next
