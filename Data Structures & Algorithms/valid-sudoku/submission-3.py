class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cells = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                sq = (i//3) * 3 + j//3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in cells[sq]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                cells[sq].add(board[i][j])
        return True