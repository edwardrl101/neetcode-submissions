class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            if len(h) == k:
                if num >= h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h, num)
            # if not full
            else:
                heapq.heappush(h, num)
        return h[0]