from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                # If we find unvisited land
                if grid[i][j] > 0:
                    island_sum = 0
                    stack = [(i, j)]
                    
                    # Add the initial cell's value and mark as visited
                    island_sum += grid[i][j]
                    grid[i][j] = 0 
                    
                    # Traverse the entire island
                    while stack:
                        r, c = stack.pop()
                        
                        # Check all 4 adjacent directions
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            
                            # If adjacent cell is within bounds and is land
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark visited immediately to prevent duplicate processing
                                stack.append((nr, nc))
                                
                    # After traversing the whole island, check divisibility
                    if island_sum % k == 0:
                        count += 1
                        
        return count