class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        drops = [0] * n
        for i in range(n - 1):
            drops[i + 1] = drops[i] + (1 if nums[i] > nums[i + 1] else 0)
   
        divisors = []
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                divisors.append(k)
                if k * k != n:
                    divisors.append(n // k)
                    
        ans = 0
        for k in divisors:
            valid = True
            prev_max = -1
            
            for i in range(0, n, k):
                num_drops = drops[i + k - 1] - drops[i]
                
                if num_drops == 0:
                    cur_min = nums[i]
                    cur_max = nums[i + k - 1]
                elif num_drops == 1 and nums[i + k - 1] <= nums[i]:
                    lo, hi = i, i + k - 2
                    while lo < hi:
                        mid = (lo + hi) // 2
                        if drops[mid + 1] - drops[i] == 1:
                            hi = mid
                        else:
                            lo = mid + 1
                    cur_max = nums[lo]
                    cur_min = nums[lo + 1]
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