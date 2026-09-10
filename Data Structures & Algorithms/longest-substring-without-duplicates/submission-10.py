class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        longest = 1

        for c in s:
            while c in stack:
                stack.pop(0)
            stack.append(c)

            longest = max(longest, len(stack))
        
        return longest