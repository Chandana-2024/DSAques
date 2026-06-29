class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sum = 0
        maxi = 0
        mp ={}
        for i in range(len(arr)):
            sum = sum + arr[i];
            
            if sum == k:
                maxi = i+1;
                
            rem = sum - k
            if rem in mp:
                size = i - mp[rem]
                maxi = max(maxi,size)
            if sum not in mp:
                mp[sum] = i
                
        
        return maxi
        
    
