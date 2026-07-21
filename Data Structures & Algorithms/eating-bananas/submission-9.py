class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mn, mx = 1, max(piles)
        k = (mn+mx)//2
        while mn < mx:
            k = (mn+mx)//2
            t = 0
            for p in piles:
                t += math.ceil(p/k)
            if t > h:
                mn = k+1
            else:
                mx = k
        return mn