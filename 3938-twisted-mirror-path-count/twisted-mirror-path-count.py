class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0, 0] for _ in range(n)]
        
        for i in range(m):
            new_dp = [[0, 0] for _ in range(n)]
            if i == 0:
                new_dp[0][0] = 1
                
            for j in range(n):
                if i == 0 and j == 0:
                    ways_right = 1
                    ways_down = 1
                else:
                    from_left = new_dp[j][0]
                    from_top = dp[j][1]
                    
                    if grid[i][j] == 0:
                        total = (from_left + from_top) % MOD
                        ways_right = total
                        ways_down = total
                    else:
                        ways_right = from_top
                        ways_down = from_left
            
                if j + 1 < n:
                    new_dp[j + 1][0] = ways_right
                if i + 1 < m:
                    new_dp[j][1] = ways_down
             
                if i == m - 1 and j == n - 1:
                    return (new_dp[j][0] + dp[j][1]) % MOD
                    
            dp = new_dp
            
        return 0