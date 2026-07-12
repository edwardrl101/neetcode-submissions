class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def isOutOfBounds(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n

        def explore(r: int, c: int):
            if isOutOfBounds(r, c) or grid[r][c] == '0':
                return
            grid[r][c] = '0'

            for d in dirs:
                explore(r + d[0], c + d[1])
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    res += 1
                    explore(r, c)
        
        return res


        