class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for s in strs:
            ss = sorted(s)
            if tuple(ss) not in ht:
                ht[tuple(ss)] = [s]
            else:
                ht[tuple(ss)].append(s)
        return [ht[s] for s in ht]