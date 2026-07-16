class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:

                if nums[i] + nums[left] + nums[right] == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # 2. Move pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                    
                    # 3. Skip duplicate values for 'left' and 'right' pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1  # Sum is too small, make it larger
                else:
                    right -= 1  # Sum is too large, make it smaller
                    
        return answer
                


