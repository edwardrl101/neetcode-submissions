class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ht = defaultdict(list)
        for num in cnt:
            ht[cnt[num]].append(num)
        
        res = []
        for j in range(len(nums), 0, -1):
            for num in ht[j]:
                res.append(num)
                if len(res) == k:
                    return res
        return res