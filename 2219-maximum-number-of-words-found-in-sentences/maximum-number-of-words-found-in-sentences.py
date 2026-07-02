class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x=[]
        for i in sentences:
            y=i.split()
            x.append(len(y))

        return max(x)