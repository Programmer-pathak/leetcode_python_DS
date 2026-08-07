class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Check if t contains prime factors other than 2, 3, 5, 7
        temp_t = t
        for prime in [2, 3, 5, 7]:
            while temp_t % prime == 0:
                temp_t //= prime
        if temp_t > 1:
            return "-1"

        def get_factors(n):
            c2 = c3 = c5 = c7 = 0
            while n % 2 == 0: c2 += 1; n //= 2
            while n % 3 == 0: c3 += 1; n //= 3
            while n % 5 == 0: c5 += 1; n //= 5
            while n % 7 == 0: c7 += 1; n //= 7
            return c2, c3, c5, c7

        req2, req3, req5, req7 = get_factors(t)

        digit_factors = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0),
        }

        # Check minimum digits required to satisfy remaining factors
        def min_digits_needed(r2, r3, r5, r7):
            r2, r3 = max(0, r2), max(0, r3)
            r5, r7 = max(0, r5), max(0, r7)

            # Greedily combine into largest single-digit factors (8s, 9s, 4s, 6s)
            count8 = r2 // 3
            rem2 = r2 % 3

            count9 = r3 // 2
            rem3 = r3 % 2

            count4 = rem2 // 2
            rem2 %= 2

            count2 = rem2
            count3 = rem3

            if count2 == 1 and count3 == 1:
                count6 = 1
                count2 = count3 = 0
            else:
                count6 = 0

            return count8 + count9 + count4 + count2 + count3 + count6 + r5 + r7

        # Construct smallest suffix recursively/greedily character by character
        def min_suffix(r2, r3, r5, r7, rem_len):
            if min_digits_needed(r2, r3, r5, r7) > rem_len:
                return None
            if rem_len == 0:
                return ""

            for d in range(1, 10):
                df2, df3, df5, df7 = digit_factors[d]
                nr2, nr3 = r2 - df2, r3 - df3
                nr5, nr7 = r5 - df5, r7 - df7
                if min_digits_needed(nr2, nr3, nr5, nr7) <= rem_len - 1:
                    sub = min_suffix(nr2, nr3, nr5, nr7, rem_len - 1)
                    if sub is not None:
                        return str(d) + sub
            return None

        n = len(num)
        prefix_factors = [(0, 0, 0, 0)] * (n + 1)
        first_zero = -1

        for i in range(n):
            d = int(num[i])
            if d == 0:
                first_zero = i
                break
            f2, f3, f5, f7 = digit_factors[d]
            p2, p3, p5, p7 = prefix_factors[i]
            prefix_factors[i + 1] = (p2 + f2, p3 + f3, p5 + f5, p7 + f7)

        limit = n if first_zero == -1 else first_zero

        # 1. Try matching same length n
        for i in range(limit, -1, -1):
            p2, p3, p5, p7 = prefix_factors[i]
            r2, r3, r5, r7 = req2 - p2, req3 - p3, req5 - p5, req7 - p7

            if i == n:
                if r2 <= 0 and r3 <= 0 and r5 <= 0 and r7 <= 0:
                    return num
                continue

            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                df2, df3, df5, df7 = digit_factors[d]
                s = min_suffix(r2 - df2, r3 - df3, r5 - df5, r7 - df7, n - 1 - i)
                if s is not None:
                    return num[:i] + str(d) + s

        # 2. Try length > n
        length = n + 1
        while True:
            s = min_suffix(req2, req3, req5, req7, length)
            if s is not None:
                return s
            length += 1