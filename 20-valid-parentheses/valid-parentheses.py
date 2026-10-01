class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_bracket:
                top_element = stack.pop() if stack else '#'

                if matching_bracket[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0