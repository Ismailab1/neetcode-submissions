class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize a stack to keep track of the current combination
        stack = []
        # Initialize a list to store all valid combinations
        res = []

        # Define a helper function to perform backtracking
        def backtrack(openN, closedN):
            # If the number of open and closed parentheses both equal n,
            # it means we have a valid combination
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # If the number of open parentheses is less than n,
            # add an open parenthesis and continue backtracking
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # If the number of closed parentheses is less than the number
            # of open parentheses, add a closed parenthesis and continue backtracking
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        # Start the backtracking process with 0 open and 0 closed parentheses
        backtrack(0, 0)
        
        # Return the list of valid combinations
        return res
