class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=str(x)
        return True if y==y[::-1] else False