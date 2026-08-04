class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        mn, mx = min(nums), max(nums)
        return [x for x in range(mn, mx + 1) if x not in s]