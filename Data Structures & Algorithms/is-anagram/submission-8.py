class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sortedS = defaultdict()
        sortedT = defaultdict()

        for i in range(len(s)):
            sortedS[s[i]] = sortedS.get(s[i], 0) + 1
            sortedT[t[i]] = sortedT.get(t[i], 0) + 1
        
        return sortedS == sortedT