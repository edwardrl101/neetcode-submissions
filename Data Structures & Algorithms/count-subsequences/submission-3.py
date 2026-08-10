class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        old, new = [0] * (n+1), [0] * (n+1)
        old[n], new[n] = 1, 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    new[j] = old[j] + old[j+1]
                else:
                    new[j] = old[j]
            old, new = new, [1]*(n+1)

        return old[0]