class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Ensure i is the smaller index and j is the larger index
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        # 1. Both removed from front
        front_only = j + 1
        # 2. Both removed from back
        back_only = n - i
        # 3. One from front, one from back
        both_sides = (i + 1) + (n - j)

        return min(front_only, back_only, both_sides)