from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        cost = 0
        dq = deque()
        j = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            count = 1
            while dq and dq[-1][0] < num:
                nextNum, nextCount = dq.pop()
                count += nextCount
                cost += (num - nextNum) * nextCount
                
            dq.append((num, count))
            while cost > k:
                rightmostNum, rightmostCount = dq.popleft()
                cost -= (rightmostNum - nums[j])
                j -= 1
                if rightmostCount > 1:
                    dq.appendleft((rightmostNum, rightmostCount - 1))
                    
            ans += j - i + 1
            
        return ans