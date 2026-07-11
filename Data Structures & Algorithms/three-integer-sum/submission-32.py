class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums)-1 and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return res