class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        
        sub_window = deque()

        left = 0

        for right in range(len(nums)):
            while sub_window and nums[sub_window[-1]] < nums[right]:
                sub_window.pop()
            
            sub_window.append(right)

            if left > sub_window[0]:
                sub_window.popleft()
            
            if (right + 1) >= k:
                res.append(nums[sub_window[0]])
                left += 1
        
        return res