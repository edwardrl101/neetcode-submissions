class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+' or t ==  '-' or t == '*' or t == '/':
                second, first = s.pop(), s.pop()
                if t == '+':
                    s.append(first + second)
                elif t == '-':
                    s.append(first - second)
                elif t == '*':
                    s.append(first * second)
                else:
                    s.append(int(first/second))
            else:
                s.append(int(t))
        return s[0]