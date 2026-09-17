class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len_up_to[i] stores the minimum length of a valid subarray ending at or before index i
        min_len_up_to = [float("inf")] * n

        left = 0
        curr_sum = 0
        min_len_so_far = float("inf")
        ans = float("inf")

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window from the left if sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                curr_len = right - left + 1

                # If there exists a valid non-overlapping subarray to the left
                if left > 0 and min_len_up_to[left - 1] != float("inf"):
                    ans = min(ans, curr_len + min_len_up_to[left - 1])

                min_len_so_far = min(min_len_so_far, curr_len)

            min_len_up_to[right] = min_len_so_far

        return ans if ans != float("inf") else -1