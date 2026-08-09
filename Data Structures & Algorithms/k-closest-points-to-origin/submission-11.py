class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []

        # keep a max heap of size k
        for x, y in points:
            d = x**2 + y**2
            if len(h) >= k:
                if d < -h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (-d, [x,y]))
            else:
                heapq.heappush(h, (-d,[x,y]))
        
        for x in h:
            res.append(x[1])
        return res