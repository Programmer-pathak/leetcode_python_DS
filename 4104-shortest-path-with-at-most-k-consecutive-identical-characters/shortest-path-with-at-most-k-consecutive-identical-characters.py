import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        min_cnt = [k + 1] * n
        pq = [(0, 0, 1)]
        best_dist = [{} for _ in range(n)]
        best_dist[0][1] = 0
        
        while pq:
            d, u, c = heapq.heappop(pq)
            if u == n - 1:
                return d
    
            if c >= min_cnt[u]:
                continue
            min_cnt[u] = c
            
            for v, w in adj[u]:
                nc = c + 1 if labels[v] == labels[u] else 1
                
                if nc <= k and nc < min_cnt[v]:
                    nd = d + w
                    if nd < best_dist[v].get(nc, float('inf')):
                        best_dist[v][nc] = nd
                        heapq.heappush(pq, (nd, v, nc))
                        
        return -1