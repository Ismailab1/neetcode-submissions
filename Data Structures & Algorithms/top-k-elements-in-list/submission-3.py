class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        len_heap = 0

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            len_heap += 1
            if len_heap > k:
                heapq.heappop(heap)
                len_heap -= 1

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res