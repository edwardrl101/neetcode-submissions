class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp(i): can s[i:] be split into words from wordDict?
        memo = {}
        def dp(i: int) -> bool:
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            can = False
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    if dp(j+1):
                        memo[j+1] = True
                        return True
            memo[i] = False
            return memo[i]
        
        return dp(0)