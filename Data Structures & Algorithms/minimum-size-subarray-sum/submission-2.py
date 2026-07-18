class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        cursum = 0
        res = 0
        while r < len(nums):
            cursum += nums[r]
            while cursum >= target:
                res = min(r-l+1, len(nums)) if res == 0 else min(r-l+1, res)
                print(res)
                cursum -= nums[l]
                l += 1
            r += 1
        return res