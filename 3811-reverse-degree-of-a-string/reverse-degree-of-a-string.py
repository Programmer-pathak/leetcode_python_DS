class Solution:
  def reverseDegree(self, s: str) -> int:
    ans = 0
    for idx, char in enumerate(s, start=1):
      rev_alpha = 26 - (ord(char) - ord('a'))
      ans += rev_alpha * idx
    return ans