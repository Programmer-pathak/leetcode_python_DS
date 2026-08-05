class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 1: Find all suspicious methods using DFS/BFS
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
                    
        # Step 2: Check if any non-suspicious node invokes a suspicious node
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Impossible to remove suspicious methods, return all methods
                return list(range(n))
                
        # Step 3: Return all non-suspicious methods
        return [i for i in range(n) if i not in suspicious]