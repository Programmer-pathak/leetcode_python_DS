class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res = []
        cur = [""]

        for char in expression:
            if char.isalpha():
                cur = [word + char for word in cur]
            elif char == '{':
                stack.append(res)
                stack.append(cur)
                res = []
                cur = [""]

            elif char == '}':
                prev_cur = stack.pop()
                prev_res = stack.pop()
                group_set = set(res + cur)
                cur = [p + g for p in prev_cur for g in group_set]
                res = prev_res

            elif char == ',':
                res.extend(cur)
                cur = [""]

        return sorted(list(set(res + cur)))