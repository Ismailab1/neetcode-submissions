class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        
        operators = set(['+', '-', '*','/'])
        values = []

        for i in range(len(tokens)):
            if tokens[i] in operators:
                val1 = values.pop()
                val2 = values.pop()

                if tokens[i] == '+':
                    values.append(val2 + val1)
                elif tokens[i] == '-':
                    values.append(val2 - val1)
                elif tokens[i] == '/':
                    values.append((int(float(val2) / val1)))
                else:
                    values.append(int(val2) * int(val1))
            
            else:
                values.append(int(tokens[i]))
        
        return values[0]