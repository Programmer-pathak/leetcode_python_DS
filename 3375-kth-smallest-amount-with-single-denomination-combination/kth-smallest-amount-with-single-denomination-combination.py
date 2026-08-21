import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Step 1: Remove redundant coins (e.g., if 3 is present, 6, 9, etc. add no new multiples)
        coins.sort()
        filtered_coins = []
        for x in coins:
            if not any(x % y == 0 for y in filtered_coins):
                filtered_coins.append(x)

        n = len(filtered_coins)

        # Step 2: Helper function to count numbers <= x divisible by at least one coin
        def count_divisible(target: int) -> int:
            total_count = 0
            for r in range(1, n + 1):
                sign = 1 if r % 2 == 1 else -1
                for combo in combinations(filtered_coins, r):
                    lcm_val = math.lcm(*combo)
                    total_count += sign * (target // lcm_val)
            return total_count

        # Step 3: Binary search for the smallest target where count_divisible(target) >= k
        low = 1
        high = filtered_coins[0] * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_divisible(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans