class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so basically, what we do is we create an hash to 
        # gather the counts, next we need to sort the counts and get 
        # the numbers associated with them which is not possible.
        # so, we use the counts as index and append the numbers into 
        # the list, its like a bucket
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1
        #creating bucket, dont do [[]]*n, it will create same array ref
        li=[[] for _ in range(len(nums)+1)]
        for num,count in d.items():
            li[count].append(num)
        output=[]
        for j in range(len(li)-1, -1,-1):
            for t in li[j]:
                output.append(t)
                if len(output)>=k:
                    return output