class Solution:

    def encode(self, strs: List[str]) -> str:
        # Step 1: Make sure the list is not empty
        if not strs:
            return ""

        # Step 2: Track the sizes of each word in the list and the final result of the completed encoding
        sizes, res = [], ""

        # Step 3: Appends the size of each word in the list
        for word in strs:
            sizes.append(len(word))
        
        # Step 4: Appends each word size into the result
        for sz in sizes:
            res += str(sz)
            res += ','
        
        # Step 4: When reaching the end of string sizes, add a '#' to show the actual words are beign added
        res += '#'
        
        for s in strs:
            res += s
        
        # Step 5: Return the completed encoding
        return res

    def decode(self, s: str) -> List[str]:
        # Step 1: Checks if the encoding exists
        if not s:
            return []
        
        # Step 2: Track the size of each string, the result list we need after, and the current position of our pointer (i)
        sizes, words, i = [], [], 0
        
        # Step 4: Traverse through the sizes portion of the encoding
        while s[i] != '#':
            # Step 4.1: Resets the curr string to track the current size we need for the assocated string
            curr = ""
            # Step 4.2: Tracks and appends the size of the string we need to decode
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            # Step 4.3: Iterates the pointr to the next position
            i += 1

        # Step 5: Moves the pointer to the strings portion
        i += 1

        # Step 6: Iterates through the list of sizes to append the correct string to our result list
        for sz in sizes:
            # Step 6.1: Appends the needed string using the size of the associated string
            words.append(s[i:i + sz])
            # Step 6.2: Move the poitner to the next string using the size
            i += sz
        # Step 7: Returns the decoded list
        return words

