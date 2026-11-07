import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Heap of available servers: stores tuples of (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # Heap of busy servers: stores tuples of (free_time, weight, index)
        busy_servers = []
        
        ans = []
        t = 0  # current time
        
        for j, task_time in enumerate(tasks):
            # Time can't be earlier than the task's arrival time `j`
            t = max(t, j)
            
            # If no servers are available, fast-forward time to when the next server frees up
            if not free_servers:
                t = busy_servers[0][0]
            
            # Release all servers that have finished their tasks by time `t`
            while busy_servers and busy_servers[0][0] <= t:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
            
            # Assign the task to the best available server
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            heapq.heappush(busy_servers, (t + task_time, weight, index))
            
        return ans