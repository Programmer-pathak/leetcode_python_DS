class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer=0
        while left < right:
            score=min(height[left],height[right])*(right-left)
            answer=max(answer,score)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer