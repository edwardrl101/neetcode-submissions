class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * n for _ in range(m)]

        def isOutofBounds(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= m or c >= n 

        def search(r: int, c: int, w: str):
            if len(w) >= len(word):
                if w == word:
                    return True
                return False
            if isOutofBounds(r, c):
                return False
            if visited[r][c]:
                return
            
            visited[r][c] = True
            for d in dirs:
                found = search(r + d[0], c + d[1], w + board[r][c])
                if found:
                    break
            visited[r][c] = False
            return found

        for r in range(m):
            for c in range(n):
                found = search(r, c, "")
                if found:
                    return True
        return False


        