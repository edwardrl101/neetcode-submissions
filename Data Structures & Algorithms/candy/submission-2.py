class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        left, right = [0] * len(ratings), [0] * len(ratings)
        left[0] = 1
        right[-1] = 1

        for i in range(1, n):
            left[i] = left[i-1] + 1 if ratings[i] > ratings[i-1] else 1
            right[n-i-1] = right[n-i] + 1 if ratings[n-i-1] > ratings[n-i] else 1
        
        print(left)
        print(right)
        return sum(max(left[i], right[i]) for i in range(0, n))