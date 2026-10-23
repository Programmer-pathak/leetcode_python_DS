class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = None
        for i, val in enumerate(nums):
            if val != i:
                ans = val if ans is None else (ans & val)

        return 0 if ans is None else ans