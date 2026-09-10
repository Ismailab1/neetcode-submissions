class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        operands = ["+", "-", "*", "/"]

        for t in tokens:
            if values and t in operands:
                val2 = values.pop()
                val1 = values.pop()

                if t == "+":
                    values.append(val1 + val2)
                
                elif t == "-":
                    values.append(val1 - val2)
                
                elif t == "*":
                    values.append(val1 * val2)
                
                else:
                    values.append(int(float(val1 / val2)))
            else:
                values.append(int(t))
        
        return values[-1] if values else 0