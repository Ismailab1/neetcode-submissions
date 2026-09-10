class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         check_duplicates = set(nums)

         if len(check_duplicates) != len(nums):
            return True
         return False

