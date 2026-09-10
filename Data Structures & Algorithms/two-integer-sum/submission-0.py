class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Initialize a dictionary (hashmap) to store previously visited numbers and their indices.
        prevMap = {}  # This will map each value in the list 'nums' to its index (val -> index)

        # Step 2: Iterate through the list 'nums' with both index 'i' and value 'n'.
        for i, n in enumerate(nums):
            # Step 3: Calculate the difference 'diff' that we need to find in the list.
            diff = target - n  # 'diff' is the number needed to add to 'n' to reach 'target'
            
            # Step 4: Check if the required 'diff' is already in 'prevMap'.
            # If it is, return the index of 'diff' from 'prevMap' and the current index 'i'.
            if diff in prevMap:
                return [prevMap[diff], i]  # Found a solution, return the indices of the two numbers
            
            # Step 5: If 'diff' is not found, add the current number 'n' and its index 'i' to 'prevMap'.
            prevMap[n] = i  # Store the current number as a potential candidate for future matches
