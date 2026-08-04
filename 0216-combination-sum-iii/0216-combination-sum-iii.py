class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        path = []

        def dfs(num,total):

            if total == n and len(path) == k:
                ans.append(path[:])
                return
            
            if total > n  or len(path) > k  or num > 9:
                return 
            
            path.append(num)
            dfs(num+1, total + num)
            path.pop()

            dfs(num+1,total)

        dfs(1,0)
        return ans
                