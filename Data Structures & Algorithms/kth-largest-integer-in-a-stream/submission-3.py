import heapq
# use heapq, first keep pushing the values to heap, 
# we need kth largest(means we only want to store k elements in min heap
# and get the smallest.) push always, pop it only if length of heap is
# greater than k.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap,self.k=nums,k
        heapq.heapify(self.heap)
        while(len(self.heap) > self.k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if(len(self.heap) > self.k):
            heapq.heappop(self.heap)
        return self.heap[0]
