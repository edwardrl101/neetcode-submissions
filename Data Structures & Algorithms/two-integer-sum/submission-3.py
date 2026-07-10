class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, n in enumerate(nums):
            if target-n in ht:
                return[ht[target-n], i]
            if n not in ht:
                ht[n] = i
            
        return []