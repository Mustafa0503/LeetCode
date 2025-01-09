class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for operator in tokens:
            if(not operator in "/+-*"):
                stack.append(int(operator))
                continue
            b = stack.pop()
            a = stack.pop()
            if operator == "+":
                stack.append(a + b)
            elif operator == "-":
                stack.append(a - b)
            elif operator == "*":
               stack.append(a * b)
            elif operator == "/":
                stack.append(int(a / b) ) 
        return stack[0]