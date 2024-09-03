class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = ""
        for c in s:
            converted += self._char_to_int(c)
        
        sum = converted
        for i in range(k):
            temp = 0
            for c in sum:
                temp += int(c)
            sum = str(temp)

        return int(sum)

    def _char_to_int(self, c: str) -> str:
        assert len(c) == 1
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i, letter in enumerate(list(alphabet)):
            if c == letter:
                return str(i + 1)
