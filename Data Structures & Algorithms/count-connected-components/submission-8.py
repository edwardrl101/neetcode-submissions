class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = True
            while q:
                s = q.popleft()
                for v in adj[s]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True

        for j in range(n):
            if visited[j]:
                continue
            bfs(j)
            res += 1
        return res