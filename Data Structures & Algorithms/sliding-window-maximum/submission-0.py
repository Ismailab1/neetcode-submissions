class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        sub_window = []

        left = 0

        for right in range(len(nums)):
            sub_window.append(nums[right])

            if len(sub_window) == k:
                max_num = -10000
                
                for num in sub_window:
                    max_num = max(max_num, num)
                
                res.append(max_num)

                sub_window.pop(0)
        
        return res