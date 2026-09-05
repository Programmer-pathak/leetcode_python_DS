class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Build suffix minimum array
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        # Compute prefix max on the fly and check condition
        pref_max = 0
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suff_min[i] <= k:
                return i
                
        return -1