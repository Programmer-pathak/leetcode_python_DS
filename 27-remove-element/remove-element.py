class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left=0
        right=len(nums)-1

        while left<right:
            if nums[left]!=val:
                left+=1
            else:
                if nums[left]==val and nums[right]==val:
                    nums.pop()
                    right-=1
                if nums[left]==val and nums[right]!=val:
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
        if nums[left]==val:
            nums.pop(left)
        
        return len(nums)
                