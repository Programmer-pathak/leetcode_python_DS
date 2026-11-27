from typing import List
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n

        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)

        for i, (factor, price) in enumerate(items):
            if price > budget:
                continue

            first_gain = 1 + bonus[i]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + first_gain > dp[b]:
                    dp[b] = dp[b - price] + first_gain

            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return max(dp)