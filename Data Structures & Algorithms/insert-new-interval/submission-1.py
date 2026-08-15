class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
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