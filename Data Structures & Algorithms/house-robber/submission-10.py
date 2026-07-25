class Solution:
    def rob(self, nums: List[int]) -> int:
        v = {}
        def dp(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in v:
                return v[i]
            v[i] = max(nums[i] + dp(i+2), dp(i+1))
            return v[i]
        return max(dp(0), dp(1))