class Solution:
    def rob(self, nums: List[int]) -> int:
        # max amount of money robbing starting from house i
        n = len(nums)
        one, two = 0, 0
        for i in range(n-1, -1, -1):
            curr = max(one, nums[i] + two)
            one, two = curr, one
        return max(one, two)