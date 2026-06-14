class Solution:
    # apply sliding window, start both at first char, move the right one
    # over a loop, keep adding the counts to dict, we need to check
    # if the windowLen-most frequent char is less than k, if yes, keep max count
    # else, move left pointer. AAAB, if we subtract 4-3=1, which is B, 
    # we can replace it with A, so it should be less than k.
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxi=0
        d={}
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            windowLen=r-l+1
            if(windowLen - max(d.values()) <= k):
                maxi=max(maxi, windowLen) 
            else:
                d[s[l]]=d.get(s[l],0)-1
                l+=1
        return maxi
            


