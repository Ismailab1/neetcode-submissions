class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorts the nums array to allows for two pointer solution
        res = []
        nums.sort()

        # Have one pointer go through the array like normal,
        # decreasing the size of the two pointers later for the while loop
        for i, a in enumerate(nums):
            # Makes sure the first element is always equal to
            # or below zero
            if a > 0:
                break

            # Edge case: Passes duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Sets up the two pointers for to find the sum after using the
            # a element
            l, r = i + 1, len(nums) - 1

            # Look at the two sum solution and add the extra
            # a element to the solution
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                
                elif threeSum < 0:
                    l += 1
                
                else:
                    # Appends all answers to the result array
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # while there are duplicates, we need to move the left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        # Returns the results    
        return res