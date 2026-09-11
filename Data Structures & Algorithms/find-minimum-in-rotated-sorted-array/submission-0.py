class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        rotated = 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                break
            rotated += 1

        lp, rp = 0, n

        minimum = 1001
        while lp < rp:
            mid = ((lp + (rp - lp) + rotated) % n)

            if nums[mid] < minimum:
                minimum = nums[mid]
                rp = mid - 1

            elif nums[mid] > minimum:
                rp = mid - 1

            else:
                lp = mid + 1

        return minimum