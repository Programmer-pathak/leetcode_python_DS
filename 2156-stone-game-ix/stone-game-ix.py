class Solution:

    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0] * 3
        for x in stones:
            cnt[x % 3] += 1

        if cnt[0] % 2 == 0:
            # If count of 0s is even, 0s don't change turn order/parity.
            # Alice wins if she can force Bob into a situation where he runs out of moves or makes sum divisible by 3.
            return cnt[1] > 0 and cnt[2] > 0
        else:
            # If count of 0s is odd, 0s reverse the outcome.
            return abs(cnt[1] - cnt[2]) > 2