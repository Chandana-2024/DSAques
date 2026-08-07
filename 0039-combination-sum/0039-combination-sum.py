class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def cnt(i,total):
            if total == target:
                ans.append(path[:])
                return 
            
            if total > target or i == len(nums):
                return 

            path.append(nums[i])

            cnt(i,total+nums[i])
            path.pop()
            cnt(i+1,total)
        
        cnt(0,0)
        return ans
        
