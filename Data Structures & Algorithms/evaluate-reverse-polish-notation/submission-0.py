class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        equation = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                y = equation.pop()
                x = equation.pop()
                if token == '+':
                    equation.append(x + y)
                elif token == '-':
                    equation.append(x - y)
                elif token == '*':
                    equation.append(x * y)
                elif token == '/':
                    equation.append(int(x / y))
            else:
                equation.append(int(token))
        
        return equation.pop()