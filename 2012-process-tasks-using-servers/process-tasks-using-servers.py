import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        busy_servers = []
        ans = []
        t = 0
        
        for j, task_time in enumerate(tasks):
            t = max(t, j)
            if not free_servers:
                t = busy_servers[0][0]
            while busy_servers and busy_servers[0][0] <= t:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))

            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            heapq.heappush(busy_servers, (t + task_time, weight, index))
            
        return ans