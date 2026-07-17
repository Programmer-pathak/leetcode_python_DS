class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Alphabetically sort karenge
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        ans = ""
        
        # Sirf pehli aur aakhri string ko compare karenge
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
            
        return ans