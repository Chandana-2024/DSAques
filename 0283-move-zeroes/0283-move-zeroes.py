class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(1,n):
            if nums[i] != 0 and nums[j] == 0 :
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
            if nums[j] != 0 :
                j += 1
        
            
        