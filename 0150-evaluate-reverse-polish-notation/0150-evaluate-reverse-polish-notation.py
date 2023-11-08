class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        def operate(a, b, token):
            if token == '*':
                return a*b
            elif token == '+':
                return a+b
            elif token == '-':
                return b - a
            return int(b / a)


        for token in tokens:
            if token in '+-*/':
                a = stack.pop()
                b = stack.pop()
                result = operate(a, b, token)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]
            