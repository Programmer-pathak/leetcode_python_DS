class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1
        sum_f=0
        if n==0 or n==1:
            return n
        for i in range(n-1):
                sum_f=first+second
                first=second
                second=sum_f
        return sum_f

            
