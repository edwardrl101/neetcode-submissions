class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = 1
        div = 1
        while div < n:
            cur *= (m+div-1)
            cur //= div
            div += 1
        
        return cur