from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        def add(bit: List[int], idx: int, val: int):
            while idx <= n + 1:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query_bit(bit: List[int], idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        def range_add(l: int, r: int, val: int):
            add(bit1, l, val)
            add(bit1, r + 1, -val)
            add(bit2, l, val * (l - 1))
            add(bit2, r + 1, -val * r)
            
        def prefix_sum(idx: int) -> int:
            return query_bit(bit1, idx) * idx - query_bit(bit2, idx)
            
        def range_sum(l: int, r: int) -> int:
            return prefix_sum(r) - prefix_sum(l - 1)
            
        last_seen = {}
        cur_sq_sum = 0
        total_ans = 0
        
        for i, x in enumerate(nums, 1):
            prev = last_seen.get(x, 0)

            sum_x = range_sum(prev + 1, i)
            count = i - prev
            
            cur_sq_sum = (cur_sq_sum + 2 * sum_x + count) % MOD
            total_ans = (total_ans + cur_sq_sum) % MOD
            
            range_add(prev + 1, i, 1)
            last_seen[x] = i
            
        return total_ans