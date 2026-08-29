from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Step 1: Sort elements to identify connected components easily
        sorted_nums = sorted(nums)
        
        groups = []
        num_to_group = {}
        
        # Step 2: Build connected components (groups of elements diff <= limit)
        for num in sorted_nums:
            if not groups or num - groups[-1][-1] > limit:
                groups.append(deque())
            
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1
            
        # Step 3: Reconstruct the answer using the smallest available value in each group
        result = []
        for num in nums:
            group_idx = num_to_group[num]
            # Pop the smallest available element for this group
            result.append(groups[group_idx].popleft())
            
        return result