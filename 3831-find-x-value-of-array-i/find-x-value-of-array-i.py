class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for x in nums:
            rem = x % k
            new_dp = [0] * k
            new_dp[rem] += 1
            
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * rem) % k] += dp[r]
            
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp
            
        return ans