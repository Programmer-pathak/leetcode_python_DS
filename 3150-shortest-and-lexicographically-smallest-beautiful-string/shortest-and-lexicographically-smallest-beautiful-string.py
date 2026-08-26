class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        ones_count = 0
        left = 0

        for right in range(n):
            if s[right] == '1':
                ones_count += 1

            while ones_count == k:
                sub = s[left:right + 1]

                if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                    ans = sub

                if s[left] == '1':
                    ones_count -= 1
                left += 1

        return ans