class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        memo = {}
        # amount of possible ways to reach amount, given current total and coin i
        def dp(i, total):
            if coins[i] + total >= amount:
                if coins[i] + total == amount:
                    return 1
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            
            res = 0
            for j in range(i, len(coins)):
                res += dp(j, total + coins[i])
            memo[(i, total)] = res
            return memo[(i, total)]
        
        ways = 0
        for i in range(0, len(coins)):
            ways += dp(i, 0)
        return ways