class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        ans = 0
        for i in range(1,n):
            diff = nums[i] - nums[j]
            if diff > 0:
                ans = max(ans,diff)
            else:
                j = i
        return ans
             
            

        