class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = set()
        atlantic = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        for c in range(n):
            pacific.add((0, c))
            pacific_queue.append((0, c))

            atlantic.add((m - 1, c))
            atlantic_queue.append((m - 1, c))

        for r in range(m):
            pacific.add((r, 0))
            pacific_queue.append((r, 0))

            atlantic.add((r, n - 1))
            atlantic_queue.append((r, n - 1))

        def bfs(queue, ocean):
            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in ocean or heights[nr][nc] < heights[row][col]:
                        continue
                    ocean.add((nr, nc))
                    queue.append((nr, nc))

        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)

        return [[r, c] for r, c in pacific & atlantic]