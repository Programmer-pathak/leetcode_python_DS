class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        
        to_right = [[0] * n for _ in range(m)]
        to_down = [[0] * n for _ in range(m)]
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    to_right[r][c] = (r, c)
                    to_down[r][c] = (r, c)
                else:
                    to_right[r][c] = to_down[r + 1][c] if r + 1 < m else None
                    to_down[r][c] = to_right[r][c + 1] if c + 1 < n else None

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                ways = dp[r][c]
                if not ways or grid[r][c] == 1:
                    continue
                
                if c + 1 < n:
                    dest = to_right[r][c + 1]
                    if dest:
                        nr, nc = dest
                        dp[nr][nc] = (dp[nr][nc] + ways) % MOD
                
                if r + 1 < m:
                    dest = to_down[r + 1][c]
                    if dest:
                        nr, nc = dest
                        dp[nr][nc] = (dp[nr][nc] + ways) % MOD

        return dp[m - 1][n - 1]