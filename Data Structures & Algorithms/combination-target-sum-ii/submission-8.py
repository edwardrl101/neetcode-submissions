class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(idx: int, total: int, summands: List[int]):
            if total >= target:
                if total == target:
                    res.append(summands[:])
                return

            for i in range(idx, len(candidates)):
                if i >0 and i != idx and candidates[i] == candidates[i-1]:
                    continue
                summands.append(candidates[i])
                dfs(i+1, total+candidates[i], summands)
                summands.pop()
                

        dfs(0, 0, [])
        return res