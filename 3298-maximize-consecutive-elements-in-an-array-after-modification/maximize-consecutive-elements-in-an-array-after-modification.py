from collections import defaultdict
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        ans = 0

        for x in nums:
            # Compute transitions based on values before `x` is placed
            len_inc = dp[x] + 1      # x becomes x + 1, extending sequence ending at x
            len_same = dp[x - 1] + 1  # x stays x, extending sequence ending at x - 1

            if len_inc > dp[x + 1]:
                dp[x + 1] = len_inc
            if len_same > dp[x]:
                dp[x] = len_same

            ans = max(ans, dp[x + 1], dp[x])

        return ans