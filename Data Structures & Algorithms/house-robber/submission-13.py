class Solution:
    def rob(self, nums: List[int]) -> int:
        # max amount of money robbing starting from house i
        memo = {}
        def dp(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            # skip this house, or rob it
            memo[i] = max(dp(i+1), nums[i] + dp(i+2))
            return memo[i]
        return max(dp(0),dp(1))