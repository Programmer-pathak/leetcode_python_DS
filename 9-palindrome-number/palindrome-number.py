class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        st=str(x)
        if st==st[::-1]:
            return True
        else:
            return False