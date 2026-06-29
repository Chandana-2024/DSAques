class Solution:
    def findUnion(self, a, b):
        # code here
        a.extend(b)
        uni = list(set(a))
        uni.sort()
        return uni
        
        