class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o: int, c: int, p: str):
            if c > o:
                return
            if c == n:
                res.append(p[:])
                return
            
            
            if o < n:
                backtrack(o + 1, c, p + '(')
            backtrack(o, c + 1, p +')')

        backtrack(0, 0, "")
        return res