from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()

        # Add every treasure cell as a BFS starting point.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Only visit unassigned land cells.
                if grid[nr][nc] != 2**31 - 1:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))