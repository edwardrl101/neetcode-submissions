class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        if n == 1:
            return one
        if n == 2:
            return two
        
        for _ in range(n-2):
            one, two = two, one + two
        return two