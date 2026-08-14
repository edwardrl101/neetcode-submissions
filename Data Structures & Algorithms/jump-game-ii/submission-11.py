class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        cnt = 0
        n = len(nums)
        while cur < n-1:
            if cur + nums[cur] >= n-1:
                return cnt+1
            mx, mxi = 0, cur+1
            for k in range(cur+1, min(n, cur+nums[cur]+1)):
                if k+nums[k] >= mx:
                    mx = k+nums[k]
                    mxi = k
            cur = mxi
            cnt += 1
        return cnt