class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset: List[int], idx: int):
            if idx == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[idx])
            dfs(subset, idx + 1)
            subset.pop()
            dfs(subset, idx + 1)

        dfs([], 0)
        return res