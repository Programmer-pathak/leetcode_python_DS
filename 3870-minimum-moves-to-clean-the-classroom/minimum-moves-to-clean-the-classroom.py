from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r = start_c = -1
        litter_coords = []
        
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litter_coords.append((r, c))
                    
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        full_mask = (1 << len(litter_coords)) - 1
        
        if full_mask == 0:
            return 0 

        q = deque([(start_r, start_c, 0, energy, 0)])
        
        max_energy = {}
        max_energy[(start_r, start_c, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c, mask, e, steps = q.popleft()
            
            
            if e < max_energy.get((r, c, mask), -1):
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = e - 1
                    
                    if next_e < 0:
                        continue
                        
                    next_mask = mask
                    cell = classroom[nr][nc]
                    

                    if cell == 'L':
                        bit = litter_map[(nr, nc)]
                        next_mask |= (1 << bit)
                                          
                    if next_mask == full_mask:
                        return steps + 1
                        
                    
                    if cell == 'R':
                        next_e = energy
                        
                    
                    state = (nr, nc, next_mask)
                    if next_e > max_energy.get(state, -1):
                        max_energy[state] = next_e
                        q.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1