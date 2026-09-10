class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the string is nonexistent, we return 0
        if not s:
            return 0
        
        # If the string si full of duplicates, we return 1
        if all(element == s[0] for element in s):
            return 1
        
        # Tracks the longest substring size
        longest_substring_size = 1
        
        # Tracks the current substring
        substring = deque()

        # Iterates through the string in O(n) time
        for right in range(len(s)):
            # If the current character is in the substring, we pop the elements in the 
            # substring until we remove the duplicate element
            while s[right] in substring:
                substring.popleft()
            # We add the current character to the substring
            substring.append(s[right])
            # We compare the current length of the substring to the current 
            # longest length we have recorded for the solution
            longest_substring_size = max(longest_substring_size, len(substring))
        # We return the longest substring size after iterating through the entire string    
        return longest_substring_size

        # Time complexity: O(n) time as we only iterate through the string once
        # Space complexity: O(n) space as we eventually hav ethe set store every part of the string
