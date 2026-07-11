class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        lookup = set(nums)
        for num in nums:
            cur = 1
            if num-1 not in lookup:
                nxt = num+1
                while nxt in lookup:
                    cur += 1
                    nxt += 1
                res = max(cur, res)
        return res
                    

