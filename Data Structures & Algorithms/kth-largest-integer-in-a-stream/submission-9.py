class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = nums
        self.h = heapq.nlargest(k, self.l)
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        self.l.append(val)
        print(self.h)
        if len(self.h) == self.k:
            if val >= self.h[0]:
                heapq.heappop(self.h)
                heapq.heappush(self.h, val)
        else:
            heapq.heappush(self.h, val)
        return self.h[0]
        
