class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sset=set()
        maxl=0
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l+=1
            sset.add(s[r])
            maxl=max(maxl, len(sset))
        return maxl