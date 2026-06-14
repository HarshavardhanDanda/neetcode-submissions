import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        heap=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for value,count in d.items():
            heapq.heappush(heap, (count, value))

            if len(heap) >k:
                heapq.heappop(heap)
        output=[]
        for i in heap:
            output.append(i[1])
        return output