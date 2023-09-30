class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            k=nums.index(i)
            if i==target:
                return nums.index(i)
            elif (target<nums[k]):
                return k
            elif (k<len(nums)-1 and i<target and nums[k+1]> target):
                return k+1
            elif(k==(len(nums)-1)):
                return k+1
            
