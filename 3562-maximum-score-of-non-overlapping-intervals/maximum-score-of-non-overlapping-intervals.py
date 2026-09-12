from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store original index: (l, r, weight, orig_idx)
        A = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        starts = [x[0] for x in A]

        # dp[k][i] stores (max_weight, sorted_indices_list) 
        # considering suffix A[i:] with up to k intervals
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for i in range(n - 1, -1, -1):
            l_i, r_i, w_i, idx_i = A[i]
            
            # Binary search for the first interval starting strictly after r_i
            next_idx = bisect_right(starts, r_i)

            for k in range(1, 5):
                # Option 1: Skip interval i
                best_weight, best_indices = dp[k][i + 1]

                # Option 2: Take interval i
                take_weight, take_indices = dp[k - 1][next_idx]
                cand_weight = w_i + take_weight
                cand_indices = sorted(take_indices + [idx_i])

                # Compare Option 2 against Option 1
                if cand_weight > best_weight:
                    dp[k][i] = (cand_weight, cand_indices)
                elif cand_weight == best_weight:
                    if not best_indices or cand_indices < best_indices:
                        dp[k][i] = (cand_weight, cand_indices)
                    else:
                        dp[k][i] = (best_weight, best_indices)
                else:
                    dp[k][i] = (best_weight, best_indices)

        return dp[4][0][1]