class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0] * len(queries)
        active_servers = {}
        unique_count = 0
        left = 0
        right = 0
        num_logs = len(logs)
        
        for original_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            while right < num_logs and logs[right][1] <= window_end:
                server_id, time = logs[right]
                if active_servers.get(server_id, 0) == 0:
                    unique_count += 1
                active_servers[server_id] = active_servers.get(server_id, 0) + 1
                right += 1

            while left < num_logs and logs[left][1] < window_start:
                server_id, time = logs[left]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    unique_count -= 1
                left += 1
            ans[original_idx] = n - unique_count
            
        return ans