from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r = start_c = -1
        litter_coords = []
        
        # Parse grid to find 'S' and bit indices for 'L'
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
            return 0  # No litter to collect

        # Queue format: (r, c, mask, current_energy, steps)
        q = deque([(start_r, start_c, 0, energy, 0)])
        
        # Keep track of the maximum energy reached for a given (r, c, mask)
        max_energy = {}
        max_energy[(start_r, start_c, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c, mask, e, steps = q.popleft()
            
            # Prune if we already found a way to reach this state with more energy
            if e < max_energy.get((r, c, mask), -1):
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = e - 1
                    
                    # Cannot step if energy drops below 0
                    if next_e < 0:
                        continue
                        
                    next_mask = mask
                    cell = classroom[nr][nc]
                    
                    # Pickup litter
                    if cell == 'L':
                        bit = litter_map[(nr, nc)]
                        next_mask |= (1 << bit)
                        
                    # Check win condition
                    if next_mask == full_mask:
                        return steps + 1
                        
                    # Reset energy on reset tile
                    if cell == 'R':
                        next_e = energy
                        
                    # Push state if it provides strictly higher energy for this position & mask
                    state = (nr, nc, next_mask)
                    if next_e > max_energy.get(state, -1):
                        max_energy[state] = next_e
                        q.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1