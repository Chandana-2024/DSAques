class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        if not  nums:
            return 0
        
        for i in range(n):
            if nums[i] != nums[j] :
                j += 1
                nums[j] = nums[i]
        return j+1
                