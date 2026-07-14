class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        j=0
        ans  = 0
        for i in range(1,len(nums)):
            diff = nums[i] - nums[j]
            if diff > 0  :
                ans = max(ans,diff)
            else:
                j = i
        return ans