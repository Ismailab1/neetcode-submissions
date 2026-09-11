class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp, rp = 0, len(nums) - 1

        minimum = 1001
        while lp < rp:
            mid = lp + (rp - lp) // 2

            if nums[mid] > nums[rp]:
                lp = mid + 1
            else:
                rp = mid

        return nums[lp]