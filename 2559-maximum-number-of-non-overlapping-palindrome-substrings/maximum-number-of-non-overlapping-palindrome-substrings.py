class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # End index of the previously chosen palindrome
        
        # Iterate over all possible centers for palindromes of length k or k + 1
        for i in range(2 * n - 1):
            left = i // 2
            right = left + (i % 2)
            
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                
                # Check if we found a valid palindrome that doesn't overlap
                if length >= k:
                    if left > last_end:
                        ans += 1
                        last_end = right
                    break  # Stop expanding this center once a minimal valid palindrome is found
                
                left -= 1
                right += 1
                
        return ans