class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(start,path):
            if start==len(graph)-1:
                ans.append(path.copy())
            for neighboor in graph[start]:
                path.append(neighboor)
                dfs(neighboor,path)
                path.pop()
            
        dfs(0,[0])
        return ans