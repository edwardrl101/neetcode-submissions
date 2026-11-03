class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, 1))
            return 1
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)