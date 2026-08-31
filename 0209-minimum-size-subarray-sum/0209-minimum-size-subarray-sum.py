class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        n = len(nums)
        sum1 = 0
        j=0
        for i in  range(n):
            sum1 += nums[i]
            while sum1 >= target:
                ans = min(ans, i - j + 1)
                sum1 -= nums[j]
                j += 1
        
        if  ans  !=  float('inf'):
            return ans
        else:
            return 0

        
        
            