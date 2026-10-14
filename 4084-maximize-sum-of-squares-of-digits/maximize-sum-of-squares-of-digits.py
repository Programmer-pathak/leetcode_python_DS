class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > 9 * num:
            return ""
        
        ans = []
        rem_sum = sum
        for i in range(num):
            low = max(0, rem_sum - (num - 1 - i) * 9)
            high = min(9, rem_sum)
            curr = high
            ans.append(str(curr))
            rem_sum -= curr
            
        return "".join(ans)