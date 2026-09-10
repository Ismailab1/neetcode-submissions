class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Edge case: Empty list
        if not tokens:
            return 0
        
        # Using a set for ccalling the operators in O(1) time
        operators = set(['+', '-', '*','/'])
        
        # Stores the numbers in INT form to use for equations
        values = []
        
        n = len(tokens)

        for i in range(n):
            # If I find an operator, I pop the last two values seen and
            # perform the equation based on the operator found.
            # Then I push the result to the values to be used later
            if tokens[i] in operators:
                operator = tokens[i]
                val1 = values.pop()
                val2 = values.pop()
                if operator == "+":
                    result = val2 + val1
                elif operator == "-":
                    result = val2 - val1
                elif operator == "*":
                    result = val2 * val1
                elif operator == "/":
                    result = int(float(val2) / val1)
                values.append(result)
            # If no operator is found, I push the value in INT form
            # to the values stack
            else:
                values.append(int(tokens[i]))

        return values[0]