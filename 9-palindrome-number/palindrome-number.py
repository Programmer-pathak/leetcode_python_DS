class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=str(x)
        return True if int(y[-1:-(len(y)+1):-1])==x else False