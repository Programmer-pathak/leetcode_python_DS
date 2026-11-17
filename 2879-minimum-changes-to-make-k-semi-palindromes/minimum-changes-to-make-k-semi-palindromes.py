class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute divisors for each possible length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Helper to count changes to make a specific group a palindrome
        def get_palindrome_changes(sub):
            changes = 0
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    changes += 1
                left += 1
                right -= 1
            return changes

        # cost[i][j] = minimum changes to make s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                # Try all valid divisors d
                for d in divisors[length]:
                    current_changes = 0
                    # Check each of the d groups
                    for start in range(d):
                        group_chars = []
                        for idx in range(start, length, d):
                            group_chars.append(s[i + idx])
                        current_changes += get_palindrome_changes(group_chars)
                    
                    min_changes = min(min_changes, current_changes)
                
                cost[i][j] = min_changes

        # DP table to find the minimum changes to partition s[i:] into k parts
        # dp[i][parts]
        memo = {}
        
        def dp(i, parts):
            if parts == 1:
                return cost[i][n - 1]
            if i >= n:
                return float('inf')
            if (i, parts) in memo:
                return memo[(i, parts)]
            
            res = float('inf')
            # Try all possible ending points j for the first substring of the remaining part
            for j in range(i, n - parts):
                res = min(res, cost[i][j] + dp(j + 1, parts - 1))
                
            memo[(i, parts)] = res
            return res

        return dp(0, k)