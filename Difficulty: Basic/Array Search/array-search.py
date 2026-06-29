class Solution:
    def search(self, arr, x):
        # code here
        ans = -1
        for  i in range(len(arr)):
            if arr[i] == x:
                ans = i
                break
                
        
        return ans