class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,hmax=0,0
        l,r=0,len(height)-1
        water=0
        while(l<r):
            if(height[l] < height[r]):
                lmax=max(lmax, height[l])
                water+=lmax-height[l]
                l+=1
            else:
                hmax=max(hmax, height[r])
                water+=hmax-height[r]
                r-=1
        return water
        