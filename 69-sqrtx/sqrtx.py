class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        while start<=x:
            if (start+1)*(start+1) <=x:
                start+=1
            else:
                return start
                    

    