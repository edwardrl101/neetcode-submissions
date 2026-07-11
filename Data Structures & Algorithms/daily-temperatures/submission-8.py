class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for j in range(len(temperatures)):
            if not stack or temperatures[j] <= stack[-1][0]:
                stack.append((temperatures[j], j))
            else:
                while stack and temperatures[j] > stack[-1][0]:
                    tmp = stack.pop()
                    res[tmp[1]] = j - tmp[1]
                stack.append((temperatures[j], j))

        return res
        