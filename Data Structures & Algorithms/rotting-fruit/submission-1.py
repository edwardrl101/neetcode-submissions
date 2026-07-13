class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh, q = 0, deque()
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))


        while q and fresh:
            cur = len(q)
            while cur:
                nr, nc = q.popleft()
                for dr, dc in dirs:
                    row, col = nr + dr, nc + dc
                    if not (0 <= row < m and 0 <= col < n) or grid[row][col] != 1:
                        continue
                    q.append((row, col))
                    fresh -= 1
                    grid[row][col] = 2
                cur -= 1
            res += 1
        if fresh:
            return -1
        return res

        
        