class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Establishes our two pointers
        left = 0
        right = len(numbers) - 1

        # Checks through the entire numebrs array
        # for a pair that equals target
        while left < right:
            # Takes the sum of the elements at both pointers
            # checks if they are greater or less than target
            currSum = numbers[left] + numbers[right]

            # If the sum is greater, then we move the right pointer to
            # a lesser element
            if currSum > target:
                right -= 1
            
            # If the sum is less than, we move the left pointr to
            # a greater element
            elif currSum < target:
                left += 1

            # If the sum fails both checks, then we found our solution
            # We return the pointers in accordance to the 1-indexed array
            else:
                return [left + 1, right + 1]

        # If nothing is found, we return an empty list
        return []