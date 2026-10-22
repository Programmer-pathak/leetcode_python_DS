class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        is_inc = all(nums[(i + 1) % n] == (nums[i] + 1) % n for i in range(n))
        is_dec = all(nums[(i + 1) % n] == (nums[i] - 1) % n for i in range(n))
        
        if not is_inc and not is_dec:
            return -1
            
        idx0 = nums.index(0)
        
        if is_inc:
            return min(idx0, 2 + (n - idx0) % n)
        else:
            return min(1 + (idx0 + 1) % n, 1 + (n - 1 - idx0))