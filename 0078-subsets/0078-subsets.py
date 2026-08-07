class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        path = []

        def sets(i):
            if i == len(nums):
                ans.append(path[:])
                return 
            path.append(nums[i])
            sets(i+1)
            path.pop()
            sets(i+1)
        
        sets(0)
        return ans
        
