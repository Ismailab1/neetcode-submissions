class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for num in nums:
            if num in duplicates:
                return True
            else:
                duplicates.add(num)
        return False