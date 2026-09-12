class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        j = 0 
        ans = 0
        for i in range(1, len(nums)):
            curr = nums[i] - nums[j]
            if curr > 0:
                ans = max(ans,curr)
            else:
                j = i 
        return ans


