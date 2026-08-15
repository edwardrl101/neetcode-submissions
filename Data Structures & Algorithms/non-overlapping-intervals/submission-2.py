class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0], -x[1]))
        cnt = 0
        cur = intervals[0]
        i = 1
        #print(intervals)
        while i < len(intervals):
            #print(f"cur:{cur}, intervals[i]:{intervals[i]}")
            if cur[1] > intervals[i][0]:
                cur = intervals[i] if intervals[i][1] < cur[1] else cur
                cnt += 1
            else:
                cur = intervals[i]
            i += 1
                
        return cnt