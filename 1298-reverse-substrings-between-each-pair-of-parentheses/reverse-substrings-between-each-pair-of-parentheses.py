class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                sub = []
                while stack and stack[-1] != "(":
                    sub.append(stack.pop())
                stack.pop()
                stack.extend(sub)
            else:
                stack.append(char)
        return "".join(stack)