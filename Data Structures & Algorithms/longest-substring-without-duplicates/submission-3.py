class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        ss=set()
        maxi=0
        while(r<len(s)):
            if(s[r] not in ss):
                ss.add(s[r])
                r+=1
            else:
                while(s[r] in ss):
                    ss.remove(s[l])
                    l+=1
            maxi=max(r-l, maxi)
            print(ss)
        return maxi
