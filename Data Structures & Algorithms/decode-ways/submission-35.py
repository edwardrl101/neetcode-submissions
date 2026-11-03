class Solution:
    def numDecodings(self, s: str) -> int:
        # dp(i) in how many ways can s[i:] be decoded?
        memo = {}
        def dp(i: int) -> int:
            if i >= len(s):
                # base case: one way to decode empty string
                return 1
            if i in memo:
                return memo[i]
            if int(s[i]) == 0:
                return 0
            ans = 0
            if i + 1 < len(s):
                if 0 < int(s[i:i+2]) <= 26:
                    ans += dp(i+2)
            if int(s[i]) > 0:
                ans += dp(i+1)
            memo[i] = ans
            return memo[i]
        return dp(0)