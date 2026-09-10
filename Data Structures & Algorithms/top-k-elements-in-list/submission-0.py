class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Initializes a counter

        for num in nums:
            count[num] = 1 + count.get(num, 0) # Gets the count for each num in nums
        
        heap = [] # Initializes a heap for keeping track of k elements

        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # Pushes the current num and its count into the heap
            if len(heap) > k:
                heapq.heappop(heap) # If the heap has over k elements, pops the least frequent element
        
        res = [] # Initializes a result array

        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # Appends the top K elements into the array 
        
        return res # Returns the top K elements


        