class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        cur = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            # check for overlap
            #print(f"cur:{cur}, intervals[i]:{intervals[i]}")
            if cur[1] >= intervals[i][0]:
                cur[1] = intervals[i][1] if cur[1] < intervals[i][1] else cur[1]
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res