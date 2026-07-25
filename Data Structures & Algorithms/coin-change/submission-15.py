class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        v = {}
        def dp(amt: int):
            res = float('inf')
            if amt <= 0:
                if amt == 0:
                    return 0
                return float('inf')

            if amt in v:
                return v[amt]
            
            for coin in coins:
                res = min(res, 1+dp(amt-coin))
            v[amt] = res
            return v[amt]
        res = dp(amount)
        if res == float('inf'):
            return -1
        return dp(amount)
        
        