class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        idxA = [0]*26
        idxB = [0]*26
        l, r = 0, 0
        while r < len(s1):
            idxA[ord(s1[r].lower()) - ord('a')] += 1
            idxB[ord(s2[r].lower()) - ord('a')] += 1
            r += 1
        if idxA == idxB:
            return True
  

        while r < len(s2):
            print(f"idxA:{idxA}, idxB:{idxB}")
            if idxA == idxB:
                return True
            idxB[ord(s2[r].lower())-ord('a')] += 1
            r += 1
            idxB[ord(s2[l].lower())-ord('a')] -= 1
            l += 1


        #initialize the window
        return idxA == idxB