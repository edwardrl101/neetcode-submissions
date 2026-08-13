class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # is it possible to form s3[i+j:] using interleavings of s1[i:], s2[j:]?
        if len(s1)+ len(s2) != len(s3):
            return False
        memo = {}
        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(s2):
                return s1[i] == s3[i+j] and dp(i+1, j)
            if i == len(s1):
                return s2[j] == s3[i+j] and dp(i, j+1)
            
            memo[(i, j)] = ((s1[i] == s3[i+j] and dp(i+1, j)) 
            or (s2[j] == s3[i+j] and dp(i, j+1)))
            
            return memo[(i, j)]

        return dp(0,0)

