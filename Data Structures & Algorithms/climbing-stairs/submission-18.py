class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        memo = [0] * (n+1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        def dp(i: int) -> int:
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)