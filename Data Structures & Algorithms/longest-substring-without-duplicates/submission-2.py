class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strset=set()
        maxp=0
        l=0
        for r in range(len(s)):
            while(s[r] in strset):
                strset.remove(s[l])
                l+=1
            strset.add(s[r])
            maxp=max(maxp, r-l+1)
        return maxp
