class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=[]
        double=[]
        for i in nums:
            if i>=10:
                double.append(i)
            else:
                single.append(i)
        return True if sum(single)>sum(double) or sum(single)<sum(double) else False