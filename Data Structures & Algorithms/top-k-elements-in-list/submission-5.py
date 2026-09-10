class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequencies of each num in the nums list
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Use a min-heap to pop the smallest frequency of each num
        # out of the heap
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # pushes a tuple of (frequency, num)
            if len(heap) > k:
                heapq.heappop(heap)

        # Append k elements from the heap into the result array
        # Only use the num of the tuple (frequency, num)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res