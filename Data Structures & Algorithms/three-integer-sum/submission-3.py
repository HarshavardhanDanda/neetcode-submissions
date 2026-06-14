class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums.sort()
        for i in range(len(nums)-1):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left,right=i+1,len(nums)-1
            target=-1*(nums[i])
            while(left<right):
                if((nums[left]+nums[right])<target):
                    left+=1
                    continue
                elif((nums[left]+nums[right])>target):
                    right-=1
                    continue
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while(nums[left]==nums[left-1] and left<right):
                        left+=1

        return output

