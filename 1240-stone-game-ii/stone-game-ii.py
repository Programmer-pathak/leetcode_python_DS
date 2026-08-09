class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums so we can get total remaining stones in O(1) time
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i: int, m: int) -> int:
            # Base case: if we can take all remaining piles, take them all
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            # The current player tries to maximize their score by minimizing 
            # the opponent's maximum score from the next turn.
            max_stones = 0
            for x in range(1, 2 * m + 1):
                opponent_stones = dp(i + x, max(m, x))
                current_player_stones = suffix_sum[i] - opponent_stones
                max_stones = max(max_stones, current_player_stones)
                
            memo[(i, m)] = max_stones
            return max_stones
        
        return dp(0, 1)