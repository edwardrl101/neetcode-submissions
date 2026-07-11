class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(list) for _ in range(9)]
        cols = [defaultdict(list) for _ in range(9)]
        cells = [defaultdict(list) for _ in range(9)]
        print(rows)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in cells[(i//3)*3 + j//3]:
                    return False
                rows[i][board[i][j]] = 0
                cols[j][board[i][j]] = 0
                cells[(i//3)*3 + j//3][board[i][j]] = 0
        return True