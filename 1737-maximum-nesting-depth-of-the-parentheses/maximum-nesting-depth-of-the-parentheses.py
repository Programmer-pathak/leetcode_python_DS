class Solution:
    def maxDepth(self, s: str) -> int:
        ans = current = 0
        for char in s:
            if char == '(':
                current += 1
                ans = max(ans, current)
            elif char == ')':
                current -= 1
        return ans