class Solution:
    def rob(self, nums: List[int]) -> int:
        # max amount of money robbing starting from house i
        n = len(nums)
        dp = [0] * (n+2)
        dp[-1] = dp[-2] = 0
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        return max(dp[0], dp[1])
        def dp(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            # skip this house, or rob it
            memo[i] = max(dp(i+1), nums[i] + dp(i+2))
            return memo[i]
        return max(dp(0),dp(1))