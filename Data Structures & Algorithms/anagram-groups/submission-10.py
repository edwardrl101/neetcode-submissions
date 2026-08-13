class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in strs:
            ch = sorted(s)
            ht["".join(sorted(s))].append(s)
        return [ht[x] for x in ht]