class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols = [set() for _ in range(n)]
        res = []
        dirs = [[-1, 1], [-1, -1]]

        def attackDiagonal(board, i, j):
            ni, nj = i, j
            for dx, dy in dirs:
                ni, nj = i+dx, j+dy
                while 0 <= ni < n and 0 <= nj < n:
                    if board[ni][nj] == 'Q':
                        return True
                    ni += dx
                    nj += dy
                ni, nj = i, j
            return False

        def dfs(board, i):
            if i == n:
                res.append(["".join(r) for r in board])
                return
            for j in range(0, n):
                if not('Q' in cols[j] or attackDiagonal(board, i, j)):
                    board[i][j] = 'Q'
                    cols[j].add('Q')
                    dfs(board, i+1)
                    board[i][j] = "."
                    cols[j].remove('Q')

        dfs(board, 0)
        return res