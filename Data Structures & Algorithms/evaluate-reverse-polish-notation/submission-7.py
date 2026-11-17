class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            #print(s)
            if t not in "+-*/":
                s.append(int(t))
                continue
            
            a = s.pop()
            b = s.pop()
            if t == "+":
                s.append(a+b)
            elif t == "-":
                s.append(b-a)
            elif t == "*":
                s.append(a*b)
            else:
                s.append(int(b/a))
        

        return s[0]
        