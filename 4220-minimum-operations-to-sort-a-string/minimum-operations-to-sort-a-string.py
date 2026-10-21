class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
            return 0
        
        if len(s) == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        if s[0] == mn or s[-1] == mx:
            return 1
            
        if s[0] == mx and s.count(mx) == 1 and s[-1] == mn and s.count(mn) == 1:
            return 3
            
        return 2