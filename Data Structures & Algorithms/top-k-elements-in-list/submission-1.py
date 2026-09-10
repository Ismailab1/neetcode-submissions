class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Starts a dictionary to store the counts of each number
        count = {}

        # Stores the counts of numbers in the count dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Initaializes a lits we will be using heapq to sort
        heap = []

        # Pushes each number into the heap
        # and pops the heap if the length is bigger than k
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        #  Appends the heap to a result list and returns it
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res