class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def isOutOfBounds(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n

        def explore(r: int, c: int):
            area = 1
            if isOutOfBounds(r, c) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            for dr, dc in dirs:
                area += explore(r + dr, c + dc)
            return area
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, explore(r, c))
        
        return res