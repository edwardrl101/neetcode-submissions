class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax, leftMin = 0, 0
        for c in s:
            print(c)
            if c == '(':
                leftMax += 1
                leftMin += 1
            elif c == ')':
                leftMax -= 1
                leftMin -= 1
            else:
                leftMax += 1
                leftMin -= 1
            
            leftMin = max(leftMin, 0)
            
            if leftMax < 0:
                return False
        print(f"leftmax:{leftMax}, leftmin:{leftMin}")
        return leftMin == 0