class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mx1, mx2, mx3 =0,0,0
        t1, t2, t3 = target[0], target[1], target[2]
        for i,j,k in triplets:
            if i > t1 or j > t2 or k > t3:
                continue
            mx1 = i if i == t1 else mx1
            mx2 = j if j == t2 else mx2
            mx3 = k if k == t3 else mx3
        return mx1 == t1 and mx2 == t2 and mx3 == t3