class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=s.lower()
        left=0
        right=len(s)-1
        while left<right:
            if x[left].isalnum():
                if x[right].isalnum():
                    if x[left]==x[right]:
                        left+=1
                        right-=1
                    else:
                        return False
                else:
                    right-=1
            else:
                left+=1
            
        return True