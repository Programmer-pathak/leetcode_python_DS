class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if not self.check(nums):
            return "none"
        elif nums.count(nums[0])==3 and self.check(nums):
            return "equilateral"
        elif nums.count(nums[0])==2 and self.check(nums):
            return "isosceles"
        elif nums.count(nums[1])==2 and self.check(nums):
            return "isosceles"
        else:
            return "scalene"
    def check(self,nums):
        if nums[0]+nums[1]>nums[2]:
            if nums[0]+nums[2]>nums[1]:
                if nums[1]+nums[2]>nums[0]:
                    return True