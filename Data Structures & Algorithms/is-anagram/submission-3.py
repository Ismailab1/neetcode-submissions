class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Step 1: Ensure the length of both strings are the same
        if len(s) != len(t):
            return False

        # Step 2: Make a hashMap of counts for each letter in each string
        sortedS = {}
        sortedT = {}

        for i in range(len(s)):
            sortedS[s[i]] = 1 + sortedS.get(s[i], 0)
            sortedT[t[i]] = 1 + sortedT.get(t[i], 0)
        
        # Step 3: Check if the counts match each other
        return sortedS == sortedT
