import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []  
        available = list(range(k)) 
        req_count = [0] * k
        
        import heapq
        from bisect import bisect_left, insort
        
        busy = [] 
        available = list(range(k)) 
        counts = [0] * k
        
        for idx, (arr, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                _, s_id = heapq.heappop(busy)
                insort(available, s_id)
            
            if not available:
                continue
            
            target = idx % k
            pos = bisect_left(available, target)
            
            if pos == len(available):
                pos = 0
            
            server_id = available.pop(pos)
            counts[server_id] += 1
            heapq.heappush(busy, (arr + l, server_id))
            
        max_handled = max(counts)
        return [i for i, c in enumerate(counts) if c == max_handled]