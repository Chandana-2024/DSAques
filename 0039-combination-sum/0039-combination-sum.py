class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)
        def dfs(index,total):

            if total == target:
                ans.append(path[:])
                return 
            
            if total > target or index == n:
                return 
            
            path.append(candidates[index])

            dfs(index,total+candidates[index])

            path.pop()

            dfs(index+1,total)

        dfs(0,0)
        return ans