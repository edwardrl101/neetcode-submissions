class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        # dp[j] = dp[i+1][j]
        dp = [False] * (n + 1)
        dp[n] = True

        for j in range(n - 1, -1, -1):
            dp[j] = s2[j] == s3[m + j] and dp[j + 1]

        for i in range(m - 1, -1, -1):
            dp[n] = s1[i] == s3[i + n] and dp[n]

            for j in range(n - 1, -1, -1):
                ans = False
                
                ans = ans or (s1[i] == s3[i + j] and dp[j])

                ans = ans or (s2[j] == s3[i + j] and dp[j + 1])

                dp[j] = ans

        return dp[0]