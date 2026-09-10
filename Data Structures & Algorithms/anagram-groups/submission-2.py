class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary where each value is a list
        res = defaultdict(list)

        # Iterate over each string in the input list
        for s in strs:
            # Create a list of 26 zeros, each index representing a character in the alphabet
            count = [0] * 26
            # Iterate over each character in the string
            for c in s:
                # Update the count for the respective character
                count[ord(c) - ord('a')] += 1
            # Append the original string to the list in the dictionary
            # The key is the tuple of character counts
            res[tuple(count)].append(s)
        
        # Return the grouped anagrams as a list of lists
        return list(res.values())
