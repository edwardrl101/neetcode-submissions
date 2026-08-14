class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # is it possible to form s3[i+j:] using interleavings of s1[i:], s2[j:]?
        if len(s1)+ len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[m][n] = True
        for j in range(n-1, -1, -1):
            dp[m][j] = s2[j] == s3[m+j]

        for i in range(m-1, -1, -1):
            dp[i][n] = s1[i] == s3[i+n]
        print(dp)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                ans = False
                if i < len(s1) and s1[i] == s3[i + j]:
                    ans = ans or dp[i+1][j]

                if j < len(s2) and s2[j] == s3[i + j]:
                    ans = ans or dp[i][j+1]
                dp[i][j] = ans
        print(dp)
        return dp[0][0]
        memo = {}
        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            ans = False

            if i < len(s1) and s1[i] == s3[i + j]:
                ans = ans or dp(i + 1, j)

            if j < len(s2) and s2[j] == s3[i + j]:
                ans = ans or dp(i, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0,0)

