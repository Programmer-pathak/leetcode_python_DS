class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # min_suffix[i] stores min(nums[i..n-1])
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])
        
        # Iterate left-to-right to track max(nums[0..i])
        max_prefix = 0
        for i in range(n):
            max_prefix = max(max_prefix, nums[i])
            
            # Instability score: max(nums[0..i]) - min(nums[i..n-1])
            if max_prefix - min_suffix[i] <= k:
                return i
                
        return -1