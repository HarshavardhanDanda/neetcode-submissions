class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            li=[0]*26
            for j in i:
                li[ord(j)-97]+=1
            key=tuple(li)
            if key not in d:
                d[key]=[]
            d[key].append(i)
        return list(d.values())
        #first create emtpy array of 0s and 1s, increase the counts
        # as needed, then we need to use the list as tuple(because list cant 
        # be used as a key since its mutable), append the strings as values
