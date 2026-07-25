class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        for i in range(n-3, -1, -1):
            nums[i] = max(nums[i] + nums[i+2], nums[i+1])
        return max(nums[1], nums[0])