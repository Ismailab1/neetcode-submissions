class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initializes a dictionary to store the anagrams
        groups = defaultdict(list)

        # For each word, we sort the word into a 
        # unique key and append the current word 
        # to that key 
        for word in strs:
            sorted_word = "".join(sorted(word))

            groups[sorted_word].append(word) 
        
        # We return a list of all the groups that were sorted into
        # the dictionary
        return list(groups.values())