class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        max_val = max(diff) if diff else 0
        count = [0] * (max_val + 2)
        for d in diff:
            count[d] += 1
            
        total_k = k1 + k2
        
        for d in range(max_val, 0, -1):
            if count[d] == 0:
                continue
     
            take = min(total_k, count[d])
            total_k -= take
            count[d] -= take
            count[d - 1] += take
            
            if total_k == 0:
                break 

        if total_k > 0:
            return 0
            
        ans = 0
        for d in range(max_val + 1):
            if count[d] > 0:
                ans += count[d] * (d * d)
                
        return ans