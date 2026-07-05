class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        sum1 = nums[0]

        n = len(nums)
        ans = 0

        for  j in range(k,n):
            sum1 = max(sum1 , nums[j - k])
            ans = max(ans ,  sum1 + nums[j])
        return ans
        
        