class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        memo = {}

        def get_destination(r: int, c: int, d: int):
            if not (0 <= r < m and 0 <= c < n):
                return None
            if grid[r][c] == 0:
                return (r, c)
            
            state = (r, c, d)
            if state in memo:
                return memo[state]
            
            memo[state] = None
            if d == 0:
                res = get_destination(r + 1, c, 1)
            else:
                res = get_destination(r, c + 1, 0)
                
            memo[state] = res
            return res

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                ways = dp[r][c]
                if ways == 0 or grid[r][c] == 1:
                    continue
                
                dest_right = get_destination(r, c + 1, 0)
                if dest_right:
                    nr, nc = dest_right
                    dp[nr][nc] = (dp[nr][nc] + ways) % MOD
        
                dest_down = get_destination(r + 1, c, 1)
                if dest_down:
                    nr, nc = dest_down
                    dp[nr][nc] = (dp[nr][nc] + ways) % MOD

        return dp[m - 1][n - 1]