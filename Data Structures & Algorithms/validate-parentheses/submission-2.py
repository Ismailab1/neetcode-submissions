class Solution:
    def isValid(self, s: str) -> bool:
        # A stack to track opening parentheses
        stack = []
        # A mapping of closing to opening parentheses
        mapping = {')': '(', '}': '{', ']': '['}

        # Iterate through the string
        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the expected opening parenthesis
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening parenthesis, push it onto the stack
                stack.append(char)

        # If the stack is empty, all parentheses were matched correctly
        return not stack
