class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        lookup = set(nums)
        for num in nums:
            cnt = 0
            if num-1 not in lookup:
                cur = num
                while cur in lookup:
                    cnt += 1
                    cur += 1
            res = max(cnt,res)
        return res
                    

