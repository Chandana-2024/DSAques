class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        path = []

        n = len(s)

        def ispalindrome(l,r):

            while l < r :
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(start):

            if start == n :
                ans.append(path[:])
                return 
            
            for end in range(start , n):
                if ispalindrome(start,end):
                    path.append(s[start:end+1])
                    dfs(end+1)
                    path.pop()
        
        dfs(0)
        return ans
