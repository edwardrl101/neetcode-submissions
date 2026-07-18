class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)

        l,r = 0, 0
        res = 0
        curmax = 0
        while r < len(s):
            cnt[s[r]] += 1
            curmax = max(curmax, cnt[s[r]])
            while r-l+1-curmax > k:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
        