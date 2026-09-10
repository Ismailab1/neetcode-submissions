class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Starts a set for searching for duplicates in the nums array
        duplicates = set()

        # For each num, we check if it has been seen before and tracked in the duplicates set
        for num in nums:
            if num in duplicates: # If a duplicate is found, we return True
                return True
            duplicates.add(num) # If the number has not been seen before, we add it to the set

        return False # Returns False if no duplicate is found