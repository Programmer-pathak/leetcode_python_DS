class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the longest sequential prefix sum
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        # Step 2: Convert nums to a set for O(1) lookup
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= seq_sum
        while seq_sum in num_set:
            seq_sum += 1
            
        return seq_sum