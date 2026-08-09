class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while h:
            if len(h) >= 2:
                f = -heapq.heappop(h)
                s = -heapq.heappop(h)
                if f > s:
                    n = f-s
                    heapq.heappush(h,-n)
            else:
                return -h[0]
        
        return 0