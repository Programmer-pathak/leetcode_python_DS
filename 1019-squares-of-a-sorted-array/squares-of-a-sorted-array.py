class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right,place=n-1,n-1
        arr=[0]*n

        while left<right:
            if abs(nums[left]) < abs(nums[right]):
                arr[place]=nums[right]**2
                place-=1
                right-=1
            else:
                arr[place]=nums[left]**2
                place-=1
                left+=1
        if left==right:
            arr[place]=nums[left]**2
        
        return arr