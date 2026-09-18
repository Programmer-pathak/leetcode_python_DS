class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        intervals = []
    
        for ch in set(s):
            l = first[ch]
            r = last[ch]
            valid = True
            
            i = l
            while i <= r:
                if first[s[i]] < l:
                    valid = False
                    break
                    
                r = max(r, last[s[i]])
                i += 1
                
            if valid:
                intervals.append((r, l))
                
        # Step 3: Greedily pick non-overlapping intervals (sorted by right boundary)
        intervals.sort()
        
        result = []
        prev_end = -1
        
        for r, l in intervals:
            if l > prev_end:
                result.append(s[l : r + 1])
                prev_end = r
                
        return result