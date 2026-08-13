class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ht = defaultdict(list)
        for x in cnt:
            ht[cnt[x]].append(x)
        cnter = 0
        res = []
        for i in range(len(nums), -1, -1):
            if cnter == k:
                return res
            if i in ht:
                for x in ht[i]:
                    res.append(x)
                    cnter += 1
        return None