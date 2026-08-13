class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suf = [1] * (n), [1] * (n) 
        # suf[i] = suffix product from nums[i] (excluding nums[i])
        # pref[i] = prefix product from pref[i] (excluding nums[i])
        for i in range(1, n):
            pref[i] *= pref[i-1]*nums[i-1]
            suf[n-i-1] *= suf[n-i] * nums[n-i] 

        return [pref[i]*suf[i] for i in range(n)]