import heapq
from collections import defaultdict
from typing import List

class DualHeap:
    def __init__(self, k_small: int):
        self.max_heap = []
        self.min_heap = []
        self.delayed = defaultdict(int)
        
        self.k_small = k_small
        self.size_max = 0
        self.size_min = 0
        self.sum_max = 0
        self.sum_min = 0

    def prune(self, heap, is_max: bool):
        while heap:
            val = -heap[0] if is_max else heap[0]
            if self.delayed[val] > 0:
                self.delayed[val] -= 1
                heapq.heappop(heap)
            else:
                break

    def balance(self):
        if self.size_max > self.k_small:
            val = -heapq.heappop(self.max_heap)
            self.sum_max -= val
            heapq.heappush(self.min_heap, val)
            self.sum_min += val
            self.size_max -= 1
            self.size_min += 1
            self.prune(self.max_heap, True)
        elif self.size_max < self.k_small and self.size_min > 0:
            val = heapq.heappop(self.min_heap)
            self.sum_min -= val
            heapq.heappush(self.max_heap, -val)
            self.sum_max += val
            self.size_max += 1
            self.size_min -= 1
            self.prune(self.min_heap, False)

    def add(self, num: int):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            self.sum_max += num
            self.size_max += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.sum_min += num
            self.size_min += 1
        self.balance()

    def remove(self, num: int):
        self.delayed[num] += 1
        median = -self.max_heap[0]
        if num <= median:
            self.size_max -= 1
            self.sum_max -= num
            if num == median:
                self.prune(self.max_heap, True)
        else:
            self.size_min -= 1
            self.sum_min -= num
            self.prune(self.min_heap, False)
        self.balance()

    def get_cost(self) -> int:
        median = -self.max_heap[0]
        cost_left = self.size_max * median - self.sum_max
        cost_right = self.sum_min - self.size_min * median
        return cost_left + cost_right


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        k_small = (x + 1) // 2
        dh = DualHeap(k_small)

        costs = [0] * n
        for i in range(n):
            dh.add(nums[i])
            if i >= x:
                dh.remove(nums[i - x])
            if i >= x - 1:
                costs[i] = dh.get_cost()

        dp = [float('inf')] * (k + 1)
        dp[0] = 0
        history = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        history[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                history[i][j] = history[i - 1][j]

            if i >= x:
                cost = costs[i - 1]
                for j in range(1, k + 1):
                    if history[i - x][j - 1] != float('inf'):
                        history[i][j] = min(history[i][j], history[i - x][j - 1] + cost)

        return history[n][k]