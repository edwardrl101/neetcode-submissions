class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate the time it takes to reach target
        combined = (list(zip(position, speed)))
        combined.sort(key=lambda x: -x[0])
        stack = []
        for c in combined:
            p, s = c[0], c[1]
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)