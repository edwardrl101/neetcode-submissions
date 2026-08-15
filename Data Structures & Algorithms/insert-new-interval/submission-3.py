class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)-1
        while l <= r:
            m = l + (r-l)//2
            if intervals[m][0] == newInterval[0]:
                l = m
                break
            elif intervals[m][0] > newInterval[0]:
                r = m-1
            else:
                l = m+1
        intervals.insert(l, newInterval)
        cur = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if cur[1] >= intervals[i][0]:
                cur[1] = intervals[i][1] if cur[1] < intervals[i][1] else cur[1]
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res
