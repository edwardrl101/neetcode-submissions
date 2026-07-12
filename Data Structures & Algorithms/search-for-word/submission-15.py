class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * n for _ in range(m)]

        def isOutofBounds(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n 

        def search(r: int, c: int, i: int):
            if i == len(word):
                return True
            if isOutofBounds(r, c) or visited[r][c] or board[r][c] != word[i]:
                return False
            visited[r][c] = True
            for d in dirs:
                found = search(r + d[0], c + d[1], i+1)
                if found:
                    break
            visited[r][c] = False
            return found

        for r in range(m):
            for c in range(n):
                found = search(r, c, 0)
                if found:
                    return True
        return False


        