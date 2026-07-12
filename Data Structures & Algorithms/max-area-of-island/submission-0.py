class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cells = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def isOutOfBounds(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n

        def explore(r: int, c: int):
            if isOutOfBounds(r, c) or grid[r][c] == 0:
                return
            cells.add((r, c))
            grid[r][c] = 0

            for dr, dc in dirs:
                explore(r + dr, c + dc)
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    explore(r, c)
                    res = max(res, len(cells))
                    cells = set()
        
        return res