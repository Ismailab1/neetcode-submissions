class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Sets a left pointer and a right pointer to compare
        # each character of the string with. Starts both pointers
        # at opposite ends of the string
        lp = 0
        rp = len(s) - 1

        # We check each character until both pointers pass each other
        # which means the string si a palindorme
        while lp <= rp:
            # If either character at the pointer is a non-alphanumeric character,
            # we log that in the console and skip it
            while lp < rp and not s[lp].isalnum():
                print(f"Skipping {s[lp]} at position {lp}")
                lp += 1
            
            while rp > lp and not s[rp].isalnum():
                print(f"Skipping {s[rp]} at position {rp}")
                rp -= 1
            
            # We check the the characters at both pointers and if
            # both characters are not the same, we end the function as this means the string
            # is not a palindrome
            print(f"Checking lp = {s[lp]} and rp = {s[rp]}")

            if s[lp].lower() != s[rp].lower():
                return False
            
            # Increments the left pointner and decrements the right pointer
            # to continue the function
            lp += 1
            rp -= 1
        
        # Returns true if there were no inconsistencies found in the string
        return True