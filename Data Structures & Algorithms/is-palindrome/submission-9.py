class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
            elif not s[rp].isalnum():
                rp -= 1
            
            elif s[rp].lower() == s[lp].lower():
                lp += 1
                rp -= 1
            
            else:
                return False
            
        
        return True