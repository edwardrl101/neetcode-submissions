class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mn, mx = max(weights), sum(weights)
        k = (mn+mx)//2
        while mn < mx:
            k = (mn+mx)//2
            print(k)
            cur = k
            t = 0
            for w in weights:
                if cur >= w:
                    cur -= w
                else:
                    t += 1
                    cur = k - w
            t += 1
            print(t)
            if t > days:
                mn = k+1
            else:
                mx = k
        return mn