class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        summands = []
        nums.sort()
        def dfs(idx: int, total: int):
            if total >= target:
                if total == target:
                    res.append(summands.copy())
                return
            
            for i in range(idx, len(nums)):
                summands.append(nums[i])
                dfs(i, total+nums[i])
                summands.pop()
        
        dfs(0, 0)
        return res