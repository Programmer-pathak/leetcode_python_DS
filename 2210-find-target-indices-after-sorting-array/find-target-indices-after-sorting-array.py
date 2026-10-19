class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]