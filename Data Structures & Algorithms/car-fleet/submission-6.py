class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        pairs = sorted(pairs, reverse = True)
        stack = []
        for p in pairs:
            time = (target - p[0])/p[1]
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)