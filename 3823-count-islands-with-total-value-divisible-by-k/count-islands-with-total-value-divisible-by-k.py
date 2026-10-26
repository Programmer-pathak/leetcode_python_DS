from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = 0
                    stack = [(i, j)]
                    island_sum += grid[i][j]
                    grid[i][j] = 0 
                    
                    while stack:
                        r, c = stack.pop()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))
                                
                    if island_sum % k == 0:
                        count += 1
                        
        return count