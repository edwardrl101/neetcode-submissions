class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        ans = 0
        cnt = defaultdict(int)
        mx = 0
        while r < len(s):
            cnt[s[r]] += 1
            mx = max(mx, cnt[s[r]])
            while r-l+1 > mx+k:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans