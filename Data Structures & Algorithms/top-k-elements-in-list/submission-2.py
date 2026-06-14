class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        counts=[[] for i in range(len(nums)+1)]
        for i in nums:
            d[i]=d.get(i, 0)+1
        for value,count in d.items():
            counts[count].append(value)
        output=[]
        for i in counts:
            for j in i:
                output.append(j)
        return output[len(output)-k:len(output)]

        