class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if(len(tokens)==1):
            return int(tokens[0])
        stack = []
        val = ""
        res = 0
        for i in tokens:
            if(i == "*" or i == "-"or i == "+"or i == "/"):
                p1 = stack.pop()
                p2 = stack.pop()
                res = int(eval(p2 + i + p1))
                stack.append(str(res))
            else:
                stack.append(i)
        return res