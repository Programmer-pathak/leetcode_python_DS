from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        init_adj: List[List[int]] = [[] for _ in range(n)]
        for node in range(1, n):
            init_adj[parent[node]].append(node)

        # new_parent[x] stores the parent of x in the modified tree
        new_parent = parent[:]
        last_seen: List[int] = [-1] * 26

        def dfs_reparent(u: int) -> None:
            char_idx = ord(s[u]) - ord('a')
            prev_anc = last_seen[char_idx]

            # Closest ancestor with the same character becomes the new parent
            if u != 0 and prev_anc != -1:
                new_parent[u] = prev_anc

            last_seen[char_idx] = u
            for v in init_adj[u]:
                dfs_reparent(v)
            last_seen[char_idx] = prev_anc

        dfs_reparent(0)

        # Build the final tree from new_parent
        final_adj: List[List[int]] = [[] for _ in range(n)]
        for node in range(1, n):
            final_adj[new_parent[node]].append(node)

        ans = [0] * n

        def dfs_size(u: int) -> int:
            size = 1
            for v in final_adj[u]:
                size += dfs_size(v)
            ans[u] = size
            return size

        dfs_size(0)
        return ans