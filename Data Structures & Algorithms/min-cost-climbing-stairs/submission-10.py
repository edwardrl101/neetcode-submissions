class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp(i) min cost of climbing stairs starting from step i
        memo = [0] * (n+2)
        for i in range(n-1, -1, -1):
            memo[i] = cost[i] + min(memo[i+1], memo[i+2])

        return min(memo[0], memo[1])

        def dp(i: int) -> int:
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        return min(dp(0), dp(1))