class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        open_brackets = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_brackets += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    res += 1
                    i += 1
            
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    res += 1
    
        res += open_brackets * 2
        return res