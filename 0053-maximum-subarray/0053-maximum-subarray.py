class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -9 * (10**5)
        sum1 = 0 
        for num in nums:
            sum1 = sum1 + num
            ans = max(ans,sum1)
            if sum1 < 0 :
                sum1 = 0
            else:
                ans = max(ans,sum1)
        return ans
