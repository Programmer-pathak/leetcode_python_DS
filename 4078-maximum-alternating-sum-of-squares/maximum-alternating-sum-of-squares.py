class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort()
        n = len(squares)
        mid = n // 2
        ans = sum(squares[mid:]) - sum(squares[:mid])
        
        return ans