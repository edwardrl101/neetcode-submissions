class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+' or t ==  '-' or t == '*' or t == '/':
                second, first = int(s.pop()), int(s.pop())
                print(f"first: {first}, second:{second}")
                if t == '+':
                    s.append(first + second)
                elif t == '-':
                    s.append(first - second)
                elif t == '*':
                    s.append(first * second)
                else:
                    s.append(int(first/second))
            else:
                s.append(t)
        return int(s[0])