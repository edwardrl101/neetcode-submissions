class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        curSum = 0
        for i in range(0, len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            mx = max(mx, curSum)
        return mx