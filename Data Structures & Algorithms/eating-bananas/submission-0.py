class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1

        result = 1000000000

        while lower_bound <= upper_bound:
            k = lower_bound + (upper_bound - lower_bound) // 2

            total_hours = sum((p + k - 1) // k for p in piles)

            if total_hours <= h:
                result = min(k, result)
                upper_bound = k - 1
            
            else:
                lower_bound = k + 1

        return result



