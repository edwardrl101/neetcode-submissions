class Solution:
    def solve(self, board: List[List[str]]) -> None:
        os, visited = set(), set()
        q = deque()
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    if r == 0 or r == m-1 or c == 0 or c == n-1:
                        q.append((r, c))
                        visited.add((r, c))
                    else:
                        os.add((r, c))

        while q:
            nr, nc = q.popleft()
            for dr, dc in dirs:
                row, col = nr + dr, nc + dc
                if not (0 <= row < m and 0 <= col < n) or board[row][col] == 'X' or (row, col) in visited:
                    continue
                q.append((row, col))
                visited.add((row, col))
                os.remove((row, col))
                
                

        while os:
            row, col = os.pop()
            board[row][col] = 'X'

                    