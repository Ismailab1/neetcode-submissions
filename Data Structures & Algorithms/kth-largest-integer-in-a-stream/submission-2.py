class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k # Initialize K
        self.minHeap = nums # Initialize the minHeap array
        heapq.heapify(self.minHeap) # Heapifies the minHeap
        while len(self.minHeap) > self.k: # If the minHeap is larger than K, pop the (K + 1)th element
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # Pushes the element in the minHeap
        if len(self.minHeap) > self.k: # If the minHeap is larger than K, pop the (K + 1)th element
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # Return the top kth element of the minHeap
