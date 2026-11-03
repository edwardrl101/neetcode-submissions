class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # length of longest increasing subsequence ending at i
        memo = {}
        def dp(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            ans = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    ans = max(ans, 1 + dp(j))
            memo[i] = ans
            return memo[i]
        
        res = 0
        for i in range(0, len(nums)):
            res = max(res, dp(i))
        return res