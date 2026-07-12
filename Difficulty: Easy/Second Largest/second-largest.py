class Solution:
    def getSecondLargest(self, arr):
        # code here
        target = max(arr)
        ans = -1
        for num in arr:
            if num <target and num != target:
                ans = max(ans,num)
        return ans
                
            