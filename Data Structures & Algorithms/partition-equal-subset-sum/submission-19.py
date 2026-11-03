class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        target = s//2
        n = len(nums)

        dp = [[False] * (target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][target] = True



        for i in range(n-1, -1, -1):
            for j in range(target, -1, -1):
                if j + nums[i] <= target:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j+nums[i]]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]