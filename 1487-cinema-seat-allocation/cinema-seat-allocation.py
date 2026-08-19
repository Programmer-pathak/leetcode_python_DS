from collections import defaultdict
from typing import List


class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Group reserved seats by row
        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved[row].add(seat)

        # Each unreserved row can accommodate 2 families
        max_groups = (n - len(reserved)) * 2

        # Check rows that have reservations
        for row, seats in reserved.items():
            left = not (seats & {2, 3, 4, 5})
            right = not (seats & {6, 7, 8, 9})
            middle = not (seats & {4, 5, 6, 7})

            if left and right:
                max_groups += 2
            elif left or right or middle:
                max_groups += 1

        return max_groups