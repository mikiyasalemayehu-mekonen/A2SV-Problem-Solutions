class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    ans[i]+=1
        return ans
        
