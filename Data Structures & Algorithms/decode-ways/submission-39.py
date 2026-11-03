class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        n = len(s)
        forwardOne = 0 if s[-1] == '0' else 1
        forwardTwo = 1
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                ans = 0
            else:
                ans = forwardOne
                if i + 1 < n and 0 < int(s[i:i+2]) < 27:
                    ans += forwardTwo
            forwardOne, forwardTwo = ans, forwardOne
        return forwardOne