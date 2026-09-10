class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         duplicates = set()

         for i in range(len(nums)):
            if nums[i] in duplicates:
                return True
            duplicates.add(nums[i])
         return False