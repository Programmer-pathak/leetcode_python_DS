class Solution:
    def countKeyChanges(self, s: str) -> int:
        z=s.lower()
        count=0
        for i in range(len(z)-1):
            if z[i]!=z[i+1]:
                count+=1
        return count