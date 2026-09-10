class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creates a dictionary for storing the anagrams
        sorted_words = defaultdict(list)

        # Looks at each word and sorts it by alphabetical order 
        # then appends it to the dictionary using the sorted form of the word as the key
        # to fit the word in the group that uses its set of characters
        for word in strs:
            sorted_word = "".join(sorted(word))

            sorted_words[sorted_word].append(word)
        
        # Returns the values of the dictianary as a list
        return list(sorted_words.values())