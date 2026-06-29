class Solution:
    def getSecondLargest(self, arr):
        # code here
        target = max(arr)
        ans = -1
        for  i in range(len(arr)):
            if arr[i] < target :
                ans = max(ans, arr[i])
        
        return ans