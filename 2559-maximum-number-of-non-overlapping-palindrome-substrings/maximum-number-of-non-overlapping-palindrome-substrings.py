class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1
        
        for i in range(2 * n - 1):
            left = i // 2
            right = left + (i % 2)
            
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                if length >= k:
                    if left > last_end:
                        ans += 1
                        last_end = right
                    break
                
                left -= 1
                right += 1
                
        return ans