class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if the lengths of the two strings are different.
        # If the lengths are not the same, they cannot be anagrams, so return False immediately.
        if len(s) != len(t):
            return False
        
        # Step 2: Create two dictionaries to count the occurrences of each character in both strings.
        count_S, count_T = {}, {}  # 'count_S' will track character counts in string 's', 'count_T' in string 't'

        # Step 3: Iterate over both strings at the same time.
        for i in range(len(s)):
            # Update the character count in 's' for the current character.
            count_S[s[i]] = 1 + count_S.get(s[i], 0)  # If the character exists, increment its count, otherwise set it to 1.
            # Update the character count in 't' for the current character.
            count_T[t[i]] = 1 + count_T.get(t[i], 0)  # Similarly, increment or initialize count for string 't'.

        # Step 4: Compare the two dictionaries.
        # If the dictionaries are identical, then both strings have the same characters with the same frequencies.
        # Thus, they are anagrams. Return True if they are equal, otherwise return False.
        return count_S == count_T
