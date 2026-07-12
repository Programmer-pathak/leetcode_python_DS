class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l=0
        r=0
        u=0
        d=0
        for i in moves:
            if i=='L':
                l=moves.count(i)
            if i=='R':
                r=moves.count(i)
            if i=='U':
                u=moves.count(i)
            if i=='D':
                d=moves.count(i)
        if l==r and u==d:
            return True
        else:
            return False