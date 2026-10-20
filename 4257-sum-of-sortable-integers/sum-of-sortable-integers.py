class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        drops = [0] * n
        last_drop = [-1] * n
        for i in range(n - 1):
            is_drop = 1 if nums[i] > nums[i + 1] else 0
            drops[i + 1] = drops[i] + is_drop
            last_drop[i + 1] = i if is_drop else last_drop[i]
            
        ans = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            valid = True
            prev_max = -1
            
            for i in range(0, n, k):
                num_drops = drops[i + k - 1] - drops[i]
                
                if num_drops == 0:
                    cur_min = nums[i]
                    cur_max = nums[i + k - 1]
                elif num_drops == 1 and nums[i + k - 1] <= nums[i]:
                    drop_idx = last_drop[i + k - 1]
                    cur_max = nums[drop_idx]
                    cur_min = nums[drop_idx + 1]
                else:
                    valid = False
                    break
                    
                if cur_min < prev_max:
                    valid = False
                    break
                prev_max = cur_max
                
            if valid:
                ans += k
                
        return ans