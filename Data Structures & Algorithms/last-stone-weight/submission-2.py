import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones)==1):
            return stones[0]
        maxHeap=[]
        for i in stones:
            heapq.heappush(maxHeap, -i)
        while(len(maxHeap)>1):
            print(maxHeap)
            m1=-heapq.heappop(maxHeap)
            m2=-heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -(abs(m1-m2)))
        return -maxHeap[0]
        
        
        