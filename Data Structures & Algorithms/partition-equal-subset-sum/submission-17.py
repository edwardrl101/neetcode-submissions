class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        mem = {}
        # can we build starting from i which result in half the total sum
        def dp(i: int, cur: int) -> bool:
            if cur > s//2 or i >= len(nums):
                return False
            if cur == s//2:
                return True
            if (i, cur) in mem:
                return mem[(i, cur)]
            mem[(i, cur)] = dp(i+1, cur) or dp(i+1, cur+nums[i])
            return mem[(i,cur)]

        return dp(0, 0)