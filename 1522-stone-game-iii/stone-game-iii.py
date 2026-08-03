class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp1, dp2, dp3 represent dp[i+1], dp[i+2], dp[i+3]
        dp1 = dp2 = dp3 = 0
        
        for i in range(n - 1, -1, -1):
            res = float('-inf')
            
            # Take 1 stone
            res = max(res, stoneValue[i] - dp1)
            
            # Take 2 stones
            if i + 1 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] - dp2)
                
            # Take 3 stones
            if i + 2 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp3)
            
            dp3, dp2, dp1 = dp2, dp1, res
            
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"