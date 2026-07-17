class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        y=str(x)

        left=0
        right=len(y)-1

        while left<right:
            if left==right:
                break
            if y[left]==y[right]:
                left+=1
                right-=1
            else:
                return False
            
        return True

        # return y==y[::-1]
        