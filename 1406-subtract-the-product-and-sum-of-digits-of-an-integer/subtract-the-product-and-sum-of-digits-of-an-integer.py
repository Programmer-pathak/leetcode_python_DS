class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digit=0
        product_digit=1
        n=str(n)
        for i in n:
            sum_digit+=int(i)
            product_digit*=int(i)
        return product_digit-sum_digit