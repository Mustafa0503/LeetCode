class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for operator in tokens:
            if operator == "+":
                stack.append(stack.pop() + stack.pop())
            elif operator == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif operator == "*":
                stack.append(stack.pop() * stack.pop())
            elif operator == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b) ) 
            else:
                stack.append(int(operator))
        return stack[0]