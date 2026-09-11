from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        ans = 0

        for d1 in range(1, 10):
            if not freq[d1]:
                continue
            freq[d1] -= 1

            for d2 in range(10):
                if not freq[d2]:
                    continue
                freq[d2] -= 1

                for d3 in range(0, 10, 2):
                    if freq[d3] > 0:
                        ans += 1

                freq[d2] += 1 

            freq[d1] += 1  

        return ans