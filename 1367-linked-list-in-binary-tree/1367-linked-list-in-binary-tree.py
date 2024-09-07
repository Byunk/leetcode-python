# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == head.val and self._isSubPath(head, node):
                return True

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return False

    def _isSubPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        if not head:
            return True
        
        if not node or node.val != head.val:
            return False

        return self._isSubPath(head.next, node.left) or self._isSubPath(head.next, node.right)

        
        