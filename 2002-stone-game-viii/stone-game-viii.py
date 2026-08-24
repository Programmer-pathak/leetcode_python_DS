class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        for i in range(1, n):
            stones[i] += stones[i - 1]
            
        max_diff = stones[-1]
        
        for i in range(n - 2, 0, -1):
            max_diff = max(max_diff, stones[i] - max_diff)
            
        return max_diff