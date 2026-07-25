class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        memo = [amount + 1] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                memo[coin] = 1
        
        for i in range(amount+1):
            for coin in coins:
                if i - coin > 0:
                    memo[i] = min(memo[i-coin] + 1, memo[i])
        return memo[amount] if memo[amount] < amount + 1 else -1
        
        