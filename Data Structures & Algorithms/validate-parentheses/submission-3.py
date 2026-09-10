class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        # For each character, we check if the parenthesis is
        # a closing parenthesis and if it is, we pop the stack one element.
        # If not, we push the parenthesis into the stack

        # Iterates through the string in O(n) time
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        
        # We return true if there are no more parenthesis left in the stack 
        # after goiing through the string
        return True if not stack else False
        
