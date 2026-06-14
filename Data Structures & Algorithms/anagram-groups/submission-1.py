class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            li = [0]*26;
            for j in i:
                li[ord(j)-97]+=1
            arr = d.get(tuple(li), [])
            arr.append(i)
            d[tuple(li)]=arr
            # value.append(i)
        return list(d.values())