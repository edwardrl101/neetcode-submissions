class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp(i, amt): min number of coins needed to make
        # amount amt using coins[i:]
        memo = {}

        def dp(i: int, amt: int) -> int:
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if (i, amt) in memo:
                return memo[(i, amt)]

            ans = float('inf')
            for j in range(i, len(coins)):
                ans = min(ans, 1 + dp(j, amt - coins[j]))

            memo[(i, amt)] = ans
            return ans

        s = dp(0, amount)
        return -1 if s == float('inf') else s