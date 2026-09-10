class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {nums[0]: 0}

        for i in range(1, len(nums)):
            diff = target - nums[i]
            if diff in differences:
                return ([differences[diff], i])
            differences[nums[i]] = i
        
        return None