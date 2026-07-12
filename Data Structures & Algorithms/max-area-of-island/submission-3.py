class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def isOutOfBounds(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n

        def explore(r: int, c: int):
            area = 0
            q = deque()
            q.append((r,c))

            while q:
                nr, nc = q.popleft()
                if isOutOfBounds(nr, nc) or grid[nr][nc] == 0:
                    continue
                area += 1
                grid[nr][nc] = 0
                for dr, dc in dirs:
                    q.append((nr + dr, nc + dc))
        
            return area
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, explore(r, c))
        
        return res