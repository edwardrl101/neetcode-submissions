class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        q = deque()
        for c, p in prerequisites:
            if p in adj:
                adj[p].append(c)
            else:
                adj[p] = [c]
        
        for p in adj:
            path = set()
            q.append(p)
            while q:
                s = q.popleft()
                if s not in adj:
                    continue
                for d in adj[s]:
                    if (s, d) in path:
                        return False
                    q.append(d)
                    path.add((s, d))
        return True