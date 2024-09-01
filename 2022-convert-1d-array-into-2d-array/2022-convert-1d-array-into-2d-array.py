class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        arr = []
        row = []
        i = 0
        for elem in original:
            row.append(elem)
            i += 1
            if i == n:
                arr.append(row)
                row = []
                i = 0
        
        return arr