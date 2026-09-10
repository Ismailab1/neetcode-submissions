class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: Checks if the length of the anagrams are the same
        # If not, returns False becuase the two words cannot be anagrams if
        # they are not the same length
        if len(s) != len(t):
            return False

        # Sets up two dictionaries to track the count of each letter
        # in each word
        sortedS = defaultdict()
        sortedT = defaultdict()

        # While going through each word, we store the current
        # character in the dictionery and increase its count 
        # for how many times we see it within the word
        for i in range(len(s)):
            sortedS[s[i]] = 1 + sortedS.get(s[i], 0)
            sortedT[t[i]] = 1 + sortedT.get(t[i], 0)
        
        # We compare the dictionaries and return True if
        # both dictionaries are identical, indicating
        # that the words are anagrams fo each other
        return sortedS == sortedT