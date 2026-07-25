class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def houseRobI(l: List[int]) -> int:
            if len(l) < 2:
                return l[0]
            f, s = l[0], max(l[0], l[1])
            for i in range(2, len(l)):
                f, s = s, max(f + l[i], s)
            return max(f,s)

        return max(houseRobI(nums[0:-1]), houseRobI(nums[1:]))