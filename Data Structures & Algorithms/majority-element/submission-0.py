class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = Counter()
        n = len(nums)

        for num in nums:
            majority[num] += 1
            if majority[num] >= n / 2:
                return num
        
        return