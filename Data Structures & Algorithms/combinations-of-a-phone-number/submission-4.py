class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz" 
        }
        res = []
        def generate(idx: int, s: str):
            if idx == len(digits):
                if s:
                    res.append(s[:])
                return
            for c in mapping[digits[idx]]:
                generate(idx+1, s+c)

        generate(0, "")
        return res
