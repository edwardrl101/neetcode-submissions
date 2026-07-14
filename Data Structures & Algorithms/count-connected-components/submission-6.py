class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visiting = set()

        def dfs(src):
            if src in visiting or adj[src] == ['#']:
                return

            visiting.add(src)
            for v in adj[src]:
                dfs(v)
            visiting.remove(src)
            adj[src] = ['#']

        for j in range(n):
            if adj[j] == ['#']:
                continue
            dfs(j)
            res += 1
        return res