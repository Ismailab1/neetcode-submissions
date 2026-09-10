class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Initialize a defaultdict where each value is a list.
        # This will group anagrams together based on a unique signature (character count).
        ans = defaultdict(list)

        # Step 2: Iterate over each string in the input list 'strs'.
        for s in strs:
            # Step 3: Create a list 'count' to represent the frequency of each character in the string.
            # The list has 26 positions (for each letter of the alphabet, 'a' to 'z').
            count = [0] * 26  # Initialize a list of 26 zeros (one for each letter a-z)

            # Step 4: Count the frequency of each character in the string 's'.
            for c in s:
                # 'ord(c) - ord("a")' gives the index of the character 'c' in the alphabet (0 for 'a', 1 for 'b', etc.).
                count[ord(c) - ord("a")] += 1  # Increment the count of the current character 'c'

            # Step 5: Use the tuple of character counts as a key in the dictionary.
            # All anagrams will have the same character count tuple.
            ans[tuple(count)].append(s)  # Group the string 's' with other anagrams based on its character count
        
        # Step 6: Return the grouped anagrams as a list of lists (all values of the dictionary).
        return ans.values()
