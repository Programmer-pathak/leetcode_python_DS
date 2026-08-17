class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        # Base case for length 1
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        # Process interval length from 2 to n
        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Advance split point 'mid' where left_sum <= right_sum
                while get_sum(i, mid) < get_sum(mid + 1, j):
                    mid += 1
                
                # Case 1: left_sum < right_sum for k from i to mid-1
                res = 0
                if mid > i:
                    res = max(res, max_l[i][mid - 1])
                
                # Case 2: left_sum > right_sum for k from mid to j-1
                if mid < j:
                    res = max(res, max_r[mid + 1][j])
                    
                # Case 3: left_sum == right_sum when split exact at mid
                if get_sum(i, mid) == get_sum(mid + 1, j):
                    res = max(res, max_l[i][mid], max_r[mid + 1][j])

                dp[i][j] = res
                
                # Maintain helper max arrays
                total = get_sum(i, j)
                max_l[i][j] = max(max_l[i][j - 1], dp[i][j] + total)
                max_r[i][j] = max(max_r[i + 1][j], dp[i][j] + total)

        return dp[0][n - 1]