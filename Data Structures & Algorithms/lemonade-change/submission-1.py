class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand = 0
        freq = defaultdict(int)
        for b in bills:
            if b == 5:
                freq[b] += 1
            elif b == 10:
                if freq[5] < 1:
                    return False
                freq[b] += 1
                freq[5] -= 1
            else:
                if not (freq[5] >= 3 or (freq[5] >= 1 and freq[10] >= 1)):
                    return False
                if freq[5] >= 1 and freq[10] >= 1:
                    freq[10] -= 1
                    freq[5] -= 1
                else:
                    freq[5] -= 3
                freq[20] += 1
        return True