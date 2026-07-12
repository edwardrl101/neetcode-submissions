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
                pos = q.popleft()
                if isOutOfBounds(pos[0], pos[1]) or grid[pos[0]][pos[1]] == 0:
                    continue
                area += 1
                grid[pos[0]][pos[1]] = 0
                for dr, dc in dirs:
                    q.append((pos[0] + dr, pos[1] + dc))
        

            return area
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, explore(r, c))
        
        return res