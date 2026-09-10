class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Initialize an array to keep track of the count for each letter for each string
        res = defaultdict(list)

        # Step 2: Iterate through the list of strings
        for s in strs:
            count = [0] * 26

            # Step 3: Keep track of the count of each character in a given string
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Step 4: Add the current work to the tuple of the count of characters in string
            res[tuple(count)].append(s)

        # Step 5: Return a list of all the results (values)
        return list(res.values())