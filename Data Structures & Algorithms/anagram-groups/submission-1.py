class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #Initializes a dictionary for the values

        for s in strs:
            sortedS = ''.join(sorted(s)) # Sorts the current string for easier comparision
            res[sortedS].append(s) # Appends the original string to the index of the sorted string
        return list(res.values()) # returns a list of all the values after being group