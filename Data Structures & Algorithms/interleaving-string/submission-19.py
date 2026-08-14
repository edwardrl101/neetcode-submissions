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
            newDp = [False] * (n + 1)

            newDp[n] = s1[i] == s3[i + n] and dp[n]

            for j in range(n - 1, -1, -1):
                take_s1 = (
                    s1[i] == s3[i + j]
                    and dp[j]
                )

                take_s2 = (
                    s2[j] == s3[i + j]
                    and newDp[j + 1]
                )

                newDp[j] = take_s1 or take_s2

            dp = newDp

        return dp[0]