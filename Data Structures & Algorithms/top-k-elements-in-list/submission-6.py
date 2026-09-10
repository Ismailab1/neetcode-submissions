class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequencies of each num in the nums list
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Returns the K keys with the highest frequencies
        return heapq.nlargest(k, count.keys(), key=count.get)

        # heapq.nlargest(k, iterable, key=None)
        # ---------------------------------------------------------
        # 1. k: The number of top elements to return.
        # 2. iterable: The data source (list, dict keys, etc.).
        # 3. key: A function that specifies how to compare elements 
        #    (e.g., key=count.get to sort by dictionary values).
        #
        # Efficiency: 
        # - Best for small 'k'. Performance is O(N log k).
        # - If k=1, use max(). If k is large, use sorted()[:k].
        #
        # Usage in Top K Frequent:
        # return heapq.nlargest(k, count.keys(), key=count.get)