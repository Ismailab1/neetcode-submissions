class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Set up the suffix and prefix arrays and saves the length of the
        # nums array to use for the rest of the function
        n = len(nums)
        pref, suff, res = [0] * n, [0] * n, [0] * n

        # Sets up the first element of the prefix and the last element fo the suffix array
        # as one to ensure everything is multiplied correctly
        pref[0] = suff[n - 1] = 1

        # Stores the product of the previous element in nums and prefix
        # at the current position
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        # Stores the product of the previous element in nums and suffix
        # at the current position
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        # Gets the product of the suffix and the prefix at the current position
        # and stores it in results
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
