class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        st = 0
        end = n-1
        mid = 0
        while mid <= end:
            if nums[mid] == 0:
                nums[st],nums[mid] = nums[mid], nums[st]
                mid += 1
                st += 1
            elif nums[mid] == 2:
                nums[mid],nums[end] = nums[end],nums[mid]
                end -= 1
            else:
                mid +=1
        
        