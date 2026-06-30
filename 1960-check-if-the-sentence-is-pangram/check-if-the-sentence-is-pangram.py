class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(97,123):
            if chr(i) in sentence:
                continue
            else:
                return False
        return True
