class Solution:
    def isValid(self, s: str) -> bool:
        close = {}
        close["["] = "]"
        close ["("] = ")"
        close["{"] = "}"

        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if not stack or c != close[stack[-1]]:
                    return False
                stack.pop()
        return not stack