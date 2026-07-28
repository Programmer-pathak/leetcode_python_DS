class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid      # mid potential answer hai
                left = mid + 1 # bada square root dhoondhne ke liye aage badhein
            else:
                right = mid - 1 # square chhota karne ke liye peechhe aayein
                
        return ans

    