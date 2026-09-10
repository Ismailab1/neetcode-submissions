class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Prerequisite: Checks if the two words lengths are teh same
        # to ensure they both qualify to be anagrams
        if len(s) != len(t):
            return False

        # Sets a frequency map the length of the alphabet
        count = [0] * 26

        # Increments the frequency map with a character from S
        # and decrements the frequency map with a character from T

        # For every character in S, there should be a character in T
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # If there is any value in the frequency map OTHER THAN zero,
        # there are characters that are diferrent between the words,
        # which makes the check false
        for val in count:
            if val != 0:
                return False
            
        return True