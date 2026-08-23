class Solution:

    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        left_q = 0
        right_sum = 0
        right_q = 0

        for i in range(half):
            if num[i] == "?":
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == "?":
                right_q += 1
            else:
                right_sum += int(num[i])

        # If total number of question marks is odd, Alice can always win
        if (left_q + right_q) % 2 != 0:
            return True

        # Bob can only balance if the sum difference equals 9 * (q_difference / 2)
        return (left_sum - right_sum) != (right_q - left_q) * 9 / 2