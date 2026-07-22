class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        visited=set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(start):
            visited.add(start)
            if start==destination:
                return True
            for neighboor in graph[start]:
                if neighboor not in visited:
                    if dfs(neighboor):
                        return True
            return False
        
        return dfs(source)