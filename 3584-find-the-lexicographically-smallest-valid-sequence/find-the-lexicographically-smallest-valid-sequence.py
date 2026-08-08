class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # last_idx[j] stores the maximum index in word1 from which word2[j:]
        # can be matched as a subsequence.
        last_idx = [-1] * (m + 1)
        last_idx[m] = n
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last_idx[j] = i
                j -= 1
                
        res = []
        j = 0
        changed = False
        
        for i in range(n):
            if j == m:
                break
                
            # Case 1: Exact match
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            # Case 2: Mismatch, but we can change word1[i] to match word2[j]
            elif not changed and last_idx[j + 1] > i:
                res.append(i)
                j += 1
                changed = True
                
        return res if len(res) == m else []