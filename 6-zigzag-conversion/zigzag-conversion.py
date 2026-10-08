class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        idx = 0
        step = 1
        
        for c in s:
            rows[idx] += c
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
            
        return "".join(rows)