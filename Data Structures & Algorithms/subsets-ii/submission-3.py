class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(subset: List[int], idx: int, chosen: bool):
            if idx == len(nums):
                res.append(subset[:])
                return
            
            
            subset.append(nums[idx])
            dfs(subset, idx + 1, True)
            subset.pop()
            if idx == 0 or nums[idx] != nums[idx-1] or not chosen:
                dfs(subset, idx + 1, False)
            

        dfs([], 0, False)
        return res