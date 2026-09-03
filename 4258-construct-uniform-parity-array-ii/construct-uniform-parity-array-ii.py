class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 != 0 for x in nums1)
        
        # If all elements already have the same parity
        if not has_even or not has_odd:
            return True
        
        # If mixed, we can turn all numbers odd if the minimum element in nums1 is odd.
        # (Subtracting the smallest odd number from any even number results in an odd number).
        return min(nums1) % 2 != 0