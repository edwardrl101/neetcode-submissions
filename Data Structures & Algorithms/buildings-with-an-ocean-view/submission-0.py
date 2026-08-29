class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        suffix = [0] * len(heights)
        for j in range(len(heights)-2, -1, -1):
            suffix[j] = max(heights[j+1], suffix[j+1])

        return [i for i in range(0, len(heights)) if heights[i] > suffix[i]]