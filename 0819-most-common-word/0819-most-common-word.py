class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^A-Za-z ]+', ' ', paragraph)
        paragraph = re.sub('[ ]+', ' ', paragraph)
        paragraph = paragraph.strip()
        words = paragraph.split(" ")
        print(words)
        c = Counter(words)
        for mc, _ in c.most_common():
            if mc not in banned:
                return mc

        raise NotImplementedError