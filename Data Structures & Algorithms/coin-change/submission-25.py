class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # dp(i, amt): min number of coins needed to make
        # amount amt using coins[i:]
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        # dp[i] - min no. of coins needed to make amount i using array coins
        for c in coins:
            if c <= amount:
                dp[c] = 1

        for i in range(0, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return dp[amount] if dp[amount] != amount + 1 else -1


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