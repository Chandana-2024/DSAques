class Solution:
    def leaders(self, arr):
        # code here
        ans = []
        res = float('-inf')
        
        for i in  range(len(arr)-1,-1,-1):
            if arr[i] >= res:
                res = max(res, arr[i])
                ans.append(arr[i])
            
        ans.reverse()
        return ans
            
            
            