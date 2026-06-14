class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]
        for i in range(len(nums)-1):
            if( i >0 and nums[i] == nums[i-1]):
                continue
            target=nums[i]*-1 #two sum
            a=i+1
            b=len(nums)-1
            while(a<b):
                if(nums[a]+nums[b]<target):
                    a+=1
                    continue
                elif(nums[a]+nums[b]>target):
                    b-=1
                    continue
                else:
                    output.append([nums[i], nums[a], nums[b]])
                    a+=1
                    # b-=1
                    # nums=[-2,0,0,2,2]
                    while(a<b and nums[a]==nums[a-1]):
                        a+=1
        return output
