class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        for path in paths:
            if path and path != ".." and path != ".":
                stack.append(path)
            elif stack and path == "..":
                stack.pop()
        return "/" + "/".join(stack)
