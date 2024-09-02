class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        r = k % s

        for i, c in enumerate(chalk):
            r = r - c
            if r < 0:
                return i
        
        raise Exception
