import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = nums[i]
            g = nums[i]
            lcm = nums[i]

            for j in range(i + 1, n):
                val = nums[j]
                prod *= val
                g = math.gcd(g, val)
                lcm = math.lcm(lcm, val)

                if prod == lcm * g:
                    ans = max(ans, j - i + 1)

        return ans