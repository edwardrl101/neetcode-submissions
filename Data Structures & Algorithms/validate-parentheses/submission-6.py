class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if stack and c == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack