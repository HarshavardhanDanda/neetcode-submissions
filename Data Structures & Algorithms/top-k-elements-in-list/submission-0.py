class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1
        li=[[] for _ in range(len(nums)+1)]
        for num,count in d.items():
            li[count].append(num)
        flat=[]
        for i in li:
            for t in i:
                flat.append(t)
        return(flat[len(flat)-k:])