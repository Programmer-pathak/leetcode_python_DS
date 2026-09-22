class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def _merge(self, node: int, left_child: int, right_child: int):
        self.tree_prod[node] = (self.tree_prod[left_child] * self.tree_prod[right_child]) % self.k
        
        for r in range(self.k):
            self.tree_cnt[node][r] = self.tree_cnt[left_child][r]
        
        left_prod = self.tree_prod[left_child]
        for r in range(self.k):
            cnt = self.tree_cnt[right_child][r]
            if cnt > 0:
                self.tree_cnt[node][(left_prod * r) % self.k] += cnt

    def build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            val_rem = nums[l] % self.k
            self.tree_prod[node] = val_rem
            self.tree_cnt[node][val_rem] = 1
            return

        mid = (l + r) // 2
        self.build(nums, node * 2 + 1, l, mid)
        self.build(nums, node * 2 + 2, mid + 1, r)
        self._merge(node, node * 2 + 1, node * 2 + 2)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            val_rem = val % self.k
            self.tree_prod[node] = val_rem
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][val_rem] = 1
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(node * 2 + 1, l, mid, idx, val)
        else:
            self.update(node * 2 + 2, mid + 1, r, idx, val)
        self._merge(node, node * 2 + 1, node * 2 + 2)

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_cnt[node]

        mid = (l + r) // 2
        if qr <= mid:
            return self.query(node * 2 + 1, l, mid, ql, qr)
        elif ql > mid:
            return self.query(node * 2 + 2, mid + 1, r, ql, qr)

        left_prod, left_cnt = self.query(node * 2 + 1, l, mid, ql, qr)
        right_prod, right_cnt = self.query(node * 2 + 2, mid + 1, r, ql, qr)

        res_prod = (left_prod * right_prod) % self.k
        res_cnt = list(left_cnt)

        for r_rem in range(self.k):
            if right_cnt[r_rem] > 0:
                res_cnt[(left_prod * r_rem) % self.k] += right_cnt[r_rem]

        return res_prod, res_cnt


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            seg_tree.update(0, 0, n - 1, idx, val)
            _, cnt = seg_tree.query(0, 0, n - 1, start, n - 1)
            ans.append(cnt[x])

        return ans