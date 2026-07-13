class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2^31 - 1
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def isOOB(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n

        def explore(r: int, c: int) -> None:
            visited = set()
            q = deque()
            q.append((r, c))
            visited.add((r,c))

            while q:
                nr, nc = q.popleft()
                print((nr, nc))
                for dr, dc in dirs:
                    row, col = nr + dr, nc + dc
                    if isOOB(row, col) or grid[row][col] == -1 or grid[row][col] == 0 or (row,col) in visited:
                        continue
                    grid[row][col] = min(grid[row][col], 1 + grid[nr][nc])
                    q.append((row, col))
                    visited.add((row,col))
                    # grid[nr+dr][nc+dc] is INF

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    explore(r, c)