class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0 
        ans = 0

        for i in range(n):
            if nums[i] == 1:
                cnt +=1
                ans = max(ans,cnt)
            elif nums[i] == 0:
                cnt = 0 
            ans = max(ans,cnt)    
        return ans
