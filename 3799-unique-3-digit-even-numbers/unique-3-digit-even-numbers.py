from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        ans = 0
        
        # Iterate over all candidate 3-digit even numbers
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            
            # Count frequency required for the current number
            req = Counter([d1, d2, d3])
            
            # Check if available digits satisfy the required counts
            if all(freq[d] >= count for d, count in req.items()):
                ans += 1
                
        return ans