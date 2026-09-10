class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creates a dictionary for storing the num and their index
        differences = {}

        # Checks what the difference is from the current num to the
        # target and tries to find the diff in the dictionary. Otherwise,
        # we sstore the index of the current num in the dictionary
        for i, num in enumerate(nums):
            diff = target - num

            if diff in differences:
                return [differences[diff], i]
            differences[num] = i
        