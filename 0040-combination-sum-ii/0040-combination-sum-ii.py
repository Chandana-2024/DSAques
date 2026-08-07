class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = []
        path = []

        def dfs(st,total):
            if total == target:
                ans.append(path[:])
            
            if total > target:
                return

            for i in range(st,len(nums)):
                if i > st and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                dfs(i+1,total+nums[i])
                path.pop()

        dfs(0,0)
        return ans 