class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        max_count=0
        for i in arr:
            if i%2!=0:
                count+=1
            else:
                count=0
            max_count=max(max_count,count)
            
        if max_count>=3:
            return True
        else:
            return False