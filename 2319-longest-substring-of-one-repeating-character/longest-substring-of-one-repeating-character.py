class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        # Tree arrays storing node data
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.left_char = [''] * (4 * self.n)
        self.right_char = [''] * (4 * self.n)
        
        self._build(1, 0, self.n - 1)

    def _merge(self, node: int, l_child: int, r_child: int, l_len: int, r_len: int):
        self.left_char[node] = self.left_char[l_child]
        self.right_char[node] = self.right_char[r_child]
        
        # Base prefix and suffix lengths
        self.pref_len[node] = self.pref_len[l_child]
        self.suff_len[node] = self.suff_len[r_child]
        
        # Base max length is the maximum of left and right children
        self.max_len[node] = max(self.max_len[l_child], self.max_len[r_child])
        
        # If middle boundary characters match, attempt to merge across the boundary
        if self.right_char[l_child] == self.left_char[r_child]:
            cross_len = self.suff_len[l_child] + self.pref_len[r_child]
            self.max_len[node] = max(self.max_len[node], cross_len)
            
            # Extend prefix length if left child is entirely uniform
            if self.pref_len[l_child] == l_len:
                self.pref_len[node] = l_len + self.pref_len[r_child]
                
            # Extend suffix length if right child is entirely uniform
            if self.suff_len[r_child] == r_len:
                self.suff_len[node] = r_len + self.suff_len[l_child]

    def _build(self, node: int, start: int, end: int):
        if start == end:
            char = self.s[start]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.left_char[node] = char
            self.right_char[node] = char
            return
        
        mid = (start + end) // 2
        l_child, r_child = 2 * node, 2 * node + 1
        
        self._build(l_child, start, mid)
        self._build(r_child, mid + 1, end)
        
        self._merge(node, l_child, r_child, mid - start + 1, end - mid)

    def update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.s[idx] = char
            self.left_char[node] = char
            self.right_char[node] = char
            return
        
        mid = (start + end) // 2
        l_child, r_child = 2 * node, 2 * node + 1
        
        if idx <= mid:
            self.update(l_child, start, mid, idx, char)
        else:
            self.update(r_child, mid + 1, end, idx, char)
            
        self._merge(node, l_child, r_child, mid - start + 1, end - mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegmentTree(s)
        ans = []
        n = len(s)
        
        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, n - 1, idx, char)
            ans.append(tree.max_len[1])
            
        return ans