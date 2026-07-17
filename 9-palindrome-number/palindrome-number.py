class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        return False if x<0 else(True if y==y[::-1] else False)