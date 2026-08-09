class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        # keep a max heap of size k
        for x, y in points:
            d = x**2 + y**2
            if len(h) >= k:
                if d < -h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (-d, [x,y]))
            else:
                heapq.heappush(h, (-d,[x,y]))
        
        return [x[1] for x in h]