class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # Step 1: Ensure the length of both strigns are the same
       if len(s) != len(t):
        return False

       # Step 2: Sort both strings
       

       # Step 3: Check if the sorted strings matches each other

       return sorted(s) == sorted(t)