class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance_value = 0
        
        for val1 in arr1:
            is_valid = True
            for val2 in arr2:
                if abs(val1 - val2) <= d:
                    is_valid = False
                    break
            if is_valid:
                distance_value += 1
                
        return distance_value