class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}
        # dp(i, a) is the number of ways to form amount a using coins from index i onwards
        def dp(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i,a) in memo:
                return memo[(i, a)]
            res = dp(i+1, a)
            if coins[i] <= a:
                res += dp(i, a-coins[i])
            memo[(i,a)] = res
            return res
            
        return dp(0, amount)