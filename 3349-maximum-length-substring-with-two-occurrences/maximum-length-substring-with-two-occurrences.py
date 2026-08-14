class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Add character at right pointer to frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Shrink window from the left if any character count exceeds 2
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len