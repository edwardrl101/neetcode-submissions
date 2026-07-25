class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        v = {}
        def dp(i: int) -> int:
            if i in v:
                return v[i]
            if i >= len(cost):
                return 0
            v[i] = min(cost[i] + dp(i+1), cost[i] + dp(i+2))
            return v[i]
        return min(dp(0), dp(1))