class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum <= 0 or sum > 9 * num:
            return ""
        
        nines, rem = divmod(sum, 9)
        if nines == num:
            return "9" * num
        
        return "9" * nines + str(rem) + "0" * (num - nines - 1)
