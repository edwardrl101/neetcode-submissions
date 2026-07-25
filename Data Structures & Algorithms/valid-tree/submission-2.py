class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj = [[] for _ in range(n)]
        visited = [False] * n
        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent or node == neighbor == parent:
                    return False

            return True

        
        res = dfs(edges[0][0], edges[0][1])
        if not res:
            return False
        for i in range(n):
            if not visited[i]:
                return False
        return True