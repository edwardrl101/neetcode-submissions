class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [-1] * len(height), [-1] * len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
            rightMax[n-i-1] = max(rightMax[n-i], height[n-i-1])
        
        area = 0
        for j in range(n):
            area += (min(leftMax[j], rightMax[j])-height[j])

        return area