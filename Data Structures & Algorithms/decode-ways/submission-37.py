class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp(i) in how many ways can s[i:] be decoded?
        dp = [0 if i < n and s[i] == '0' else 1 for i in range(n+1)]
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            ans = dp[i+1]
            if i + 1 < n and 0 < int(s[i:i+2]) < 27:
                ans += dp[i+2]
            dp[i] = ans
        return dp[0]

        memo = {}
        def dp(i: int) -> int:
            if i >= len(s):
                # base case: one way to decode empty string
                return 1
            if i in memo:
                return memo[i]
            if int(s[i]) == 0:
                return 0
            ans = dp(i+1)
            if i + 1 < len(s) and 0 < int(s[i:i+2]) <= 26:
                ans += dp(i+2)
            memo[i] = ans
            return memo[i]
        return dp(0)