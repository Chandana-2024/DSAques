class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []

        def sets(st):
            ans.append(path[:])

            for i in range(st,len(nums)):
                if i > st and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                sets(i+1)
                path.pop()
        sets(0)
        return ans
