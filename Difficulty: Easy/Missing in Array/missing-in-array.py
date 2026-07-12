class Solution:
    def missingNum(self, arr):
        arr.sort()
        n = len(arr)
        for i in range(n):
            if i+1 != arr[i]:
                return i+1
            if i+1 == arr[i]:
                continue
        return n+1