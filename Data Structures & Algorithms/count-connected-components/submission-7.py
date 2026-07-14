class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        print(adj)
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for v in adj[node]:
                dfs(v)
                visited[v] = True

        for j in range(n):
            if visited[j]:
                continue
            dfs(j)
            res += 1
        return res