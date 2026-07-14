class Solution:
    def sortColors(self, nums: List[int]) -> None:
        st = 0 
        end = len(nums) - 1
        mid = 0 
        while mid <= end:
            if nums[mid] == 0:
                nums[st],nums[mid] = nums[mid],nums[st]
                st +=1
                mid +=1
            elif nums[mid ] == 2:
                nums[end],nums[mid] = nums[mid],nums[end]
                end -= 1
            else:
                mid +=1
             
        