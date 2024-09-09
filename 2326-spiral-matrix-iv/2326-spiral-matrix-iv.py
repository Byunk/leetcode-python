# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i_direction = 0

        y, x = 0, 0
        node = head
        while node:
            matrix[y][x] = node.val
            print(x, y)

            nx, ny = x + direction[i_direction][1], y + direction[i_direction][0]
            if nx == n or ny == m or matrix[ny][nx] != -1:
                i_direction = self.turn_right(i_direction)
                nx, ny = x + direction[i_direction][1], y + direction[i_direction][0]

            x, y = nx, ny
            node = node.next

        return matrix

    def turn_right(self, i):
        return (i + 1) % 4