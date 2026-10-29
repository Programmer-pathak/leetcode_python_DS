class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, 0, 0)]
        
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                timer += 1
                tin[u] = timer
                up[0][u] = p
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer
                
        for k in range(1, LOG):
            up_k = up[k]
            up_prev = up[k - 1]
            for i in range(n):
                up_k[i] = up_prev[up_prev[i]]
                
        def is_ancestor(u: int, v: int) -> bool:
            return tin[u] <= tin[v] and tout[v] <= tout[u]
            
        def get_lca(u: int, v: int) -> int:
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v
            for k in range(LOG - 1, -1, -1):
                p = up[k][u]
                if not (tin[p] <= tin[v] and tout[v] <= tout[p]):
                    u = p
            return up[0][u]
            
        bit = [0] * (n + 2)
        
        def add(idx: int, val: int):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_root_xor(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        masks = [1 << (ord(c) - 97) for c in s]
        for u in range(n):
            m = masks[u]
            add(tin[u], m)
            add(tout[u] + 1, m)
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                diff = masks[u] ^ new_mask
                if diff:
                    masks[u] = new_mask
                    add(tin[u], diff)
                    add(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                path_mask = query_root_xor(tin[u]) ^ query_root_xor(tin[v]) ^ masks[lca]
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans